import sqlite3
import os


# Function to display dashboard information
def display_dashboard_info():
    console_width = 179  
    logo = "SpotFinder"
    slogan = "Spot the Best, Park the Rest."
    contact = "For inquiries, contact: support@spotfinder.com"

    print("\n" + "=" * console_width)
    print(logo.center(console_width))
    print(slogan.center(console_width))
    print(contact.center(console_width))
    print("=" * console_width)

# Function to display menu options
def display_menu_options():
    console_width = 180  
    title = "What can we do for you?"
    options = [
        "1. Find a Spot",
        "2. Reserve your Space",
        "3. See my Bookings",
        "4. Update a Reservation",
        "5. Cancel a Reservation",
        "6. Exit"
    ]

    # Putting the option inside a box (for design)
    box_width = max(len(title), max(len(option) for option in options)) + 4
    space_before_box = (console_width - box_width) // 2 # To make the box centered in the console
    print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print top border (centered)
    print(" " * space_before_box + "| " + title.ljust(box_width - 4) + " |") # Print title left-aligned inside the box

    for option in options:
        print(" " * space_before_box + "| " + option.ljust(box_width - 4) + " |") # Print options left-aligned inside the boxes
    print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print bottom border (centered)

# Function to display the parking categories under "Find a Spot" option. 
def display_parking_categories():
    console_width = 180
    title = "SELECT A PARKING CATEGORY: "
    options = [
        "1. Regular Parking",
        "2. VIP Parking",
        "3. PWD Parking (For people with disabilities)"
    ]
    
   # Putting the option inside a box (for design)
    box_width = max(len(title), max(len(option) for option in options)) + 4
    space_before_box = (console_width - box_width) // 2 # To make the box centered in the console. 
    print("\n" + " " * space_before_box + "+" + "-" * (box_width - 2) + "+")# Print top border
    print(" " * space_before_box + "| " + title.ljust(box_width - 4) + " |") # Print title left-aligned inside the box

    for option in options:
        print(" " * space_before_box + "| " + option.ljust(box_width - 4) + " |") # Print options left-aligned inside the boxes
    print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print bottom border

# Function to display the slots in every category in a table (For design)
def display_slots_table(category, charge, slots):
    console_width = 179
    
    print("=" * console_width)
    print(f"{category} Parking".center(console_width))
    print(f"Charge rate for the first three hours: Php {charge:.2f}, Php 10.00 per additional hour".center(console_width))
    print("=" * console_width)

    # Table headers
    header = f"{'Slot Number':^90} {'Status':^85}"
    print(header)
    print("-" * console_width)

    # Display slot information in a table format
    for slot in slots:
        status = "Available" if slot[1] == "AVAILABLE" else "Reserved"
        print(f"{slot[0]:^90} {status:^85}")
    
    print("=" * console_width)

# Function to display reservation details in a table format
def display_reservation_details(reservation_id, name, vehicle_plate, mobile_number, slot_number, reservation_time):
    console_width = 179

    # Table headers
    header = f"{'Reservation ID':<30} {'Name':<40} {'Vehicle Plate':<35} {'Mobile':<35} {'Slot':<15} {'Date and Time':<15}"

    print("=" * console_width)
    print("Reservation Details".center(console_width))
    print("=" * console_width)
    print(header)
    print("-" * console_width)

    # Print the reservation details in a row
    print(f"{reservation_id:<30} {name:<40} {vehicle_plate:<35} {mobile_number:<35} {slot_number:<15} {reservation_time:<15}")
    
    print("=" * console_width)

# Database setup
def setup_database():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            vehicle_plate TEXT NOT NULL,
            mobile_number TEXT NOT NULL,
            slot_number INTEGER NOT NULL,
            reservation_time TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parking_slots (
            slot_number INTEGER PRIMARY KEY,
            category TEXT NOT NULL,
            charge_per_hour REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    # Insert parking slots if they are not already present
    cursor.execute("SELECT COUNT(*) FROM parking_slots")
    if cursor.fetchone()[0] == 0:
        slots = [(i, 'REGULAR', 25.0, 'AVAILABLE') for i in range(1, 21)] + \
                [(i, 'VIP', 90.0, 'AVAILABLE') for i in range(21, 31)] + \
                [(i, 'PWD', 0.0, 'AVAILABLE') for i in range(31, 41)]
        cursor.executemany("INSERT INTO parking_slots (slot_number, category, charge_per_hour, status) VALUES (?, ?, ?, ?)", slots)
    
    # To update the price for the first three hours of parking. 
    cursor.execute("UPDATE parking_slots SET charge_per_hour = 25.0 WHERE category = 'REGULAR'")
    cursor.execute("UPDATE parking_slots SET charge_per_hour = 95.0 WHERE category = 'VIP'")
    cursor.execute("UPDATE parking_slots SET charge_per_hour = 0.0 WHERE category = 'PWD'")
    conn.commit()
    conn.close()

# Function to view available parking reservations with category selection
def view_available_parking():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()
    
    # Calling the function to display the parking categories options. 
    display_parking_categories()
    
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        category = 'REGULAR'
    elif choice == '2':
        category = 'VIP'
    elif choice == '3':
        category = 'PWD'
    else:
        print("Invalid choice. Returning to the main menu.")
        conn.close()
        return
    
    # Now, display the available slots for the selected category
    charge = cursor.execute("SELECT charge_per_hour FROM parking_slots WHERE category=?", (category,)).fetchone()[0]
    
    # Get available slots for the selected category
    slots = cursor.execute("SELECT slot_number, status FROM parking_slots WHERE category=?", (category,)).fetchall()
    available_slots = [slot for slot in slots if slot[1] == "AVAILABLE"]
    
    # Calling the function to display the slots in a table format
    display_slots_table(category, charge, available_slots)
    
    conn.close()

# Function to reserve a parking slot
def reserve_parking():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()
    slot_number = int(input("Enter the parking slot number you want to reserve: "))
    
    # Check if the slot is available
    cursor.execute("SELECT status FROM parking_slots WHERE slot_number=?", (slot_number,))
    slot = cursor.fetchone()
    
    # If the Slot is labeled as "AVAILABLE"
    if slot and slot[0] == "AVAILABLE":
        name = input("Enter your name: ")
        vehicle_plate = input("Enter your vehicle plate number: ")
        mobile_number = input("Enter your mobile number: ")
        reservation_time = input("Enter reservation date and time (YYYY-MM-DD 00:00 PM/AM): ")

        # Update the parking slot status to "RESERVED"
        cursor.execute("UPDATE parking_slots SET status='RESERVED' WHERE slot_number=?", (slot_number,))
        
        # Insert the reservation into the reservations table
        cursor.execute("INSERT INTO reservations (name, vehicle_plate, mobile_number, slot_number, reservation_time) VALUES (?, ?, ?, ?, ?)",
                       (name, vehicle_plate, mobile_number, slot_number, reservation_time))
        
        # Get the reservation ID (the ID of the newly inserted reservation)
        reservation_id = cursor.lastrowid
        
        # Commit the changes to the database
        conn.commit()
        
        # Print a success message
        print("Parking reserved successfully!")
        
        # Display the reservation details in a table
        display_reservation_details(reservation_id, name, vehicle_plate, mobile_number, slot_number, reservation_time)
    
    # If the Slot chosen is already RESERVED. 
    else:
        print("Sorry! The parking slot is now occupied. Please select a new one.")
    
    conn.close()

# Function to view all reservations
def view_reservations():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    
    # Title to be centered
    title = "SpotFinder: Your Reservations"
 
    if not reservations:
        print("No reservations found.")
    else:
        # Print table header
        spaces = (179 - len(title)) // 2
        print(" " * spaces + title)
        print("\n" + "-" * 179)
        print(f"{'Reservation ID':<30} {'Name':<40} {'Vehicle Plate':<35} {'Mobile':<35} {'Slot':<15} {'Date and Time':<15}")
        print("-" * 179)

        # Print all the reservations made. 
        for res in reservations:
            print(f"{res[0]:<30} {res[1]:<40} {res[2] :<35} {res[3]:<35} {res[4]:<15} {res[5]:<15}")
        print("-" * 179)
    
    conn.close()

# Function to update a reservation
def update_reservation():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()

    # Display current reservations (found in "See my Bookings")
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    
    # Title to be centered in the table
    title = "ParkEase: Your Reservations"

    if not reservations:
        print("No reservations found.")
    else:
        # Print the reservation table header
        spaces = (179 - len(title)) // 2
        print(" " * spaces + title)
        print("\n" + "-" * 179)
        print(f"{'Reservation ID':<30} {'Name':<40} {'Vehicle Plate':<35} {'Mobile':<35} {'Slot':<15} {'Date and Time':<15}")
        print("-" * 179)

        # Print all the reservations made. 
        for res in reservations:
            print(f"{res[0]:<30} {res[1]:<40} {res[2] :<35} {res[3]:<35} {res[4]:<15} {res[5]:<15}")
        print("-" * 179)

        # Ask user for the reservation ID to update
        res_id = int(input("Enter your reservation ID to update: "))

        # Display options for update choice in box format
        console_width = 180
        title = "What do you want to update?"
        options = [
            "1. Name",
            "2. Vehicle Plate Number",
            "3. Mobile Number",
            "4. Reservation Date and Time",
            "5. Return to Dashboard"
        ]
        
        #Box specifications 
        box_width = max(len(title), max(len(option) for option in options)) + 4 # Calculate the box width
        space_before_box = (console_width - box_width) // 2 # The box to be centered in the console. 
        print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print top border
        print(" " * space_before_box + "| " + title.ljust(box_width - 4) + " |") # Print title left-aligned inside the box

        for option in options:
            print(" " * space_before_box + "| " + option.ljust(box_width - 4) + " |")# Print options left-aligned inside the boxes

        print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print bottom border 

        # Ask the user to select an option to update
        choice = int(input("Select an option: "))

        if choice == 1:
            new_name = input("Enter new name: ")
            cursor.execute("UPDATE reservations SET name=? WHERE id=?", (new_name, res_id))
        elif choice == 2:
            new_plate = input("Enter new vehicle plate number: ")
            cursor.execute("UPDATE reservations SET vehicle_plate=? WHERE id=?", (new_plate, res_id))
        elif choice == 3:
            new_mobile = input("Enter new mobile number: ")
            cursor.execute("UPDATE reservations SET mobile_number=? WHERE id=?", (new_mobile, res_id))
        elif choice == 4:
            new_time = input("Enter new reservation date and time (YYYY-MM-DD 00:00 PM/AM): ")
            cursor.execute("UPDATE reservations SET reservation_time=? WHERE id=?", (new_time, res_id))
        elif choice == 5:
            print("Returning to Dashboard...")
            conn.close()
            return
        else:
            print("Invalid choice.")
            conn.close()
            return

        print("Reservation updated successfully!")
        conn.commit()

    conn.close()

#Function to delete a reservation
def delete_reservation():
    conn = sqlite3.connect('parking_management.db')
    cursor = conn.cursor()

    # Display current reservations (found in "See my Bookings")
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()

    # Title to be centered 
    title = "SpotFinder: Your Reservations"

    if not reservations:
        print("No reservations found.")
    else:
        # Print the reservation table header
        spaces = (179 - len(title)) // 2
        print(" " * spaces + title)
        print("\n" + "-" * 179)
        print(f"{'Reservation ID':<30} {'Name':<40} {'Vehicle Plate':<35} {'Mobile':<35} {'Slot':<15} {'Date and Time':<15}")
        print("-" * 179)

        # Print the all the reservations made. 
        for res in reservations:
            print(f"{res[0]:<30} {res[1]:<40} {res[2] :<35} {res[3]:<35} {res[4]:<15} {res[5]:<15}")
        print("-" * 179)

        # Ask user for the reservation ID to delete
        res_id = int(input("Enter the reservation ID to cancel/delete: "))

        # Display confirmation options in box format
        console_width = 180
        title = "Are you sure you want to delete this reservation?"
        options = [
            "1. Yes",
            "2. No",
            "3. Return to Dashboard"
        ]
        
        #Box Specifications
        box_width = max(len(title), max(len(option) for option in options)) + 4 # Calculate the box width
        space_before_box = (console_width - box_width) // 2 # The box to be centered in the console.
        print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+") # Print top border
        print(" " * space_before_box + "| " + title.ljust(box_width - 4) + " |") # Print title inside the box

        for option in options:
            print(" " * space_before_box + "| " + option.ljust(box_width - 4) + " |") # Print options inside the boxes
        print(" " * space_before_box + "+" + "-" * (box_width - 2) + "+")# Print bottom border 

        # Ask the user to select an option to confirm deletion
        choice = int(input("Select an option: "))

        if choice == 1:
            # Delete the reservation and update the parking slot status
            cursor.execute("SELECT slot_number FROM reservations WHERE id=?", (res_id,))
            slot = cursor.fetchone()
            
            if slot:
                # Delete reservation from the database
                cursor.execute("DELETE FROM reservations WHERE id=?", (res_id,))
                # Set the corresponding parking slot to 'AVAILABLE'
                cursor.execute("UPDATE parking_slots SET status='AVAILABLE' WHERE slot_number=?", (slot[0],))
                print("Reservation deleted successfully!")
            else:
                print("Reservation ID not found.")
        elif choice == 2:
            print("Reservation cancelation aborted.")
        elif choice == 3:
            print("Returning to Dashboard...")
            conn.close()
            return
        else:
            print("Invalid choice. Please try again.")
            conn.close()
            return

        conn.commit()

    conn.close()

# Main function to run the system
def main():
    setup_database()
    while True:
        display_dashboard_info()
        display_menu_options()
        choice = input("Choose an option: ")

        if choice == '1':
            view_available_parking() # Function to call to view available parking
        elif choice == '2':
            reserve_parking() # Function to call to reserve a parking
        elif choice == '3':
            view_reservations() # Function to call to view reservations
        elif choice == '4':
            update_reservation() # Function to call to update a reservation
        elif choice == '5':
            delete_reservation() # Function to call to delete a reservation
        elif choice == '6':
            print("Exiting the System...") # Will terminate the whole system. 
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()