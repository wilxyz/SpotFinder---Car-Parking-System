<div align="center" style="padding-top: 5px">

<img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/SpotFinder_Logo.png" width="300" height="300"/>

## SpotFinder
*Spot the Best, Park the Rest*

**SpotFinder:** *Your number one parking buddy, to help take out the stress of seeking and managing spaces to park. Whether you require a regular, VIP, or special needs accessible parking spot, SpotFinder's always available, right at your fingertips; reservations, and plain language pricing has you covered. Our system helps you reserve your space in advance and manage and cancel bookings in a way that makes parking easy for everyone. Forget parking headaches, and say hello to easy and convenient with SpotFinder, where we make it easy to find your perfect spot with just a click!*


</div>

## Contents

<div style="margin-left: 250px; margin-right: 250px;">

- [I. Overview](#i-overview)
- [II. The Application of Python Concepts and Libraries](#ii-the-application-of-python-concepts-and-libraries)
- [III. Driving Sustainability: Integrating SDG Goals into SpotFinder](#iii-driving-sustainability-integrating-sdg-goals-into-spotfinder)
- [IV. Getting Started: How to Run SpotFinder](#iv-getting-started-how-to-run-spotfinder)

</div>

<!-- Overview of the Project starts here -->

<div style="text-align: justify;">

## I. Overview
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SpotFinder** *is a user friendly parking management system designed to simplify how you can find and reserve parking spaces. It is user friendly, efficient and accessible, where users can browse active parking slots in real time, reserve parking slots in advance and handle its bookings without any hassle. The system is inclusive and convenient for all with tailor made categories for Regular, VIP and PWD parking.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Parking slot data and reservations are stored and managed securely using an SQLite database and program logic is used to coordinate the interactions amongst cars and parking slots. The interactive console interface is an easy experience for users to view availability, update or cancel reservations and maintain efficient parking operations. It not only provides for engineers to enhance user satisfaction but also for sustainable urban development promoting smart mobility solutions.*

</div>

<div style="margin-left: 50px;">

## *Core Features*

</div> 

<div style="margin-left: 100px; margin-right: 100px; text-align: justify;">

 **1. Database Setup**
- *Creates a database (parking_management.db) with two tables:*
    - **reservations:** *Stores information about parking reservations.*
    - **parking_slots:** *Tracks parking slot details, including category, charge rate, and status.*

**2. Dashboard and User Interaction**
- *Displays a visually formatted dashboard and menu options include finding parking spots, making reservations, viewing bookings, updating or canceling reservations, and exiting the system.*

**3. Parking Slot Categories**
- *Parking slots are categories to:*
    - *Regular Parking*
    - *VIP Parking*
    - *PWD Parking*
- *Each category has its own charge rate for the first three hours and the availability status of each slots*

**4. Reservation Management**
- **View Available Parking:** *Displays the list of available parking slots per category.*
- **Reserve Parking:** *Once done viewing their preferred slot and its status, it allows user to book their reservation by entering details such as name, vehicle plate, and reservation time.*
- **View Reservations:** *Allows users to view their reservations in a table format for a cleaner and much understandable look.*
- **Update Reservations:** *Gives users a option on what to update details like name, vehicle plate, contact information, or date and time.*
- **Delete Reservations:** *Allows the users to cancel their preferred reservations and updates the slot status to "Available".*

**5. Database Updates**
- *Automatically populates the parking slots if the database is empty.*
- *Ensures consistent pricing updates for each parking category.*
- *Updates the database if the user updated his or her reservation*

**6. Error Handling**
- *Basic checks for invalid user inputs, unavailable slots or attempting to book an already reserved slot*

</div>

<!-- Overview of the Project ends here here -->

<!-- Application of Python starts here -->

## II. The Application of Python Concepts and Libraries

### Object-Oriented Programming

*The functions like `view_available_parking`, `reserve_parking`, `delete_reservation`, etc., encapsulate specific functionalities. For instance, `reserve_parking` manages user input, updates the database, and displays reservation details. Database operations are abstracted into individual functions, keeping the logic self-contained and manageable. Global state is minimized by keeping data manipulation confined within specific functions. Users interact with simple options like `"Reserve Parking"` or `"See my Bookings"` without needing to understand how the database or slot management works internally. Database setup and operations (e.g., `setup_database`, `display_slots_table`) abstract complex queries and data updates, allowing the main system logic to remain clean and focused on user interactions.*

### Database Integration

*In this system, SQLite is implemented to handle parking bookings and the slots that are available. It creates required tables such as `reservations` for storing user information and booking times and secondly, `parking_slots` for storing slot category, charges and status among others. Users can see the slots available by categories, select a slot, and whenever the slot is selected, it is updated with user details and its status changed to `“RESERVED”`. Customers also have a capacity to review, modify or delete the existing reservations and when a particular reservation is deleted, the column gets changed to `“AVAILABLE.”` SQL queries are responsible for carrying out operations within the data while Python functions stay in charge of the user interface.*

### Control Flow

*With regards to the control flow, the system reflects the basic concept of flow control through the user. Starting with database configuration where it is initiated to set up the initial database tables and data. The main menu will then appear where from choose to view parking slot, reserve a parking slot, view or update bookings, or log out of the system.*

### User Interaction

*User interaction in the system is straight forward, and the system is fully developed with menus. The users choose actions such as viewing slots, reserving, editing, or even canceling by opting for a menu number. Prompts take basic information, and tables show information in an orderly fashion. Options are given after an operation, confirmation is needed on many occasions such as cancellation, to allow for a clean user interface.* 

### Data Saving

*For data saving in the system storage, an `SQLite` database has been incorporated in the project. All reservations and parking slot details are stored persistently in two tables: `reservation` for users and bookings and `parking_slots` for available slot and charges. Whenever a user creates or modifies a reservation, the data is stored within the database using structural query language, which acts as a guarantee that the data will always be in existence. The cancellations and such or even just the slot update can also be done to the database which ensures real-time updated records.*

### Modular Design

*The functionality of the system is divided into separate, discrete, and reusable functions based on the modular approach. As mentioned, each function performs a specific function such as to display the menu, view slots, to take and input bookings or update the database. This helps to separate out the code and make it easier to read, to revise and to debug.* 

<!-- Application of Python ends here -->

<!-- SDG of the program starts here -->

## III. Driving Sustainability: Integrating SDG Goals into SpotFinder 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The **Sustainable Development Goal (SDG)** that is mostly aligned to SpotFinder is **SDG 11: Sustainable Cities and Communities**, specifically targeting **sustainable urban planning and mobility**. Here's a more detailed explanation to why this system integrates and supports SDG 11:* 

<div style="margin-left: 50px; margin-right: 50px; text-align: justify;">

- *It also supports parking slot allocation which has optimized time in finding parking. In so doing it adds to the urban mobility by reducing the traffic congestion brought about by vehicles' circular motions looking / travelling for parking.*
- **PWD Parking:** *Goals of inclusivity are met through dedicated slots for persons with disabilities (PWD) with no charges to offer the PWD equitable access to facilities.*
- *It provides access to all people to fair and transportation options available.*
- *Parking reservation control prevents idling or errant vehicle routes through the city and therefore reduces fuel consumption and emissions.*
- *This kind of system can be used in conjunction with smart city infrastructure in order to stimulate environmentally friendly transportation systems.*
- *By doing so, less spurious parking is pre reserved and more traffic flow, contributing to safer roads and communities.*

</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*This combines the work of SDG 11 by tackling urban mobility problems, encouraging inclusion, minimising environmental impact, and enhancing the support for the modern urban infrastructure. Currently developing technology for parking management, a foundation of its work can be extended to broader sustainable urban development efforts.*

<!-- SDG of the program ends here -->

<!-- How to Run SpotFinder starts here -->

## IV. Getting Started: How to Run SpotFinder

<div style="text-align: justify;">

**SpotFinder** is a type of program made from Python programming language. It is a parking management system that helps the users find available parking slots, reserve spots, view, update, and cancel reservations. This program supports a SQLite database to manage parking slot (availability status and charge per hour) and reservation data. 

## Instructions 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Follow these steps to run and interact with the program.*
</div>

<div style="margin-left: 50px; margin-right: 50px;"> 

**1. Install the Required Pre-requisites.**
- *To run the program, ensure that you have `Python 3.7` or higher installed. Also, this program uses `SQLite3` Database, in which it is pre-installed together with Python, so no additional necessary installation is required for this part.*

**2. Save the Program.**
- *Copy the program code and paste it into an empty text editor, may it be from `VS Code` or `Notepad`. Save the file and name it as `"parking_management.py"`*

**3. Create a Directory**
- *Save the file in a dedicated directory. Once the program is being executed, the `SQLite` database (`parking_management.db`) will then be created here, ensuring that the Python file and the database are in the same location.*

**4. Run the Program**
- *Open a terminal or command prompt.*
- *Navigate to the directory in which the file is saved/stored.*
```bash
cd path/to/your/script/folder
```
- *Execute the program by typing:*
```bash
python parking_management.py
```

**5. Interacting with the system.**
- **Dashboard and Menu**
    - *This program will display a dashboard and menu with options such as finding a spot, reserving a space, or exiting the system. This will prompt the user to enter the corresponding number to select an option.*
    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Main%20Dashboard.PNG" width="619px" height="251px"/>
    </p>

- **Find A Spot**
    - *This will allow the user to enter the number to view the category of parking.*
    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Find%20a%20Spot.PNG" width="1180px" height="100px"/>
    </p>

    - *This allows the user to view available slots per category.*
    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Slots.PNG" width="381px" height="231px"/>
    </p>

- **Reserve your Space**
    - *This prompts the user to enter their details such as the chosen parking slot number, their name, vehicle plate number, contact number, and the date and time of their reservation.* 
    - *After entering the details, the user will have a view of their confirmed reservation in a table format.*

    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Reserve%20a%20Slot.PNG" width="1200px" height="150px"/>
    </p>

- **See your Bookings**
    - *This allows the user to view their recent reservations.*

    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/See%20your%20Bookings.PNG" width="1200px" height="100px"/>
    </p>

- **Update your Reservation**
    - *This will prompt the user to enter the reservation ID that they've made that they want to update. After that, They will enter a number from the options on what to update on their chosen reservation which is the Name, Vehicle Plate Number, Contact Number, and the Date and Time of their Reservation.*

    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Update%20Reservation.PNG" width="1200px" height="250px"/>
    </p>

- **Cancel your Reservation**
    - *This will prompt the user to enter the reservation ID that they've made that they want to cancel. If the user wish to continue the cancellation, then the user must select the `1. Yes` option. Otherwise, if the user doesn't want to continue the cancellation or having second thoughts, then they must select the `2. No` option. Selecting `3. Return to Dashboard` will just return the user to the main dashboard of the program.*

    <p align="center">
    <img src="https://github.com/wilxyz/SpotFinder---Car-Parking-System/blob/main/ReadMe/Cancel%20Reservation.PNG" width="1200px" height="180px"/>
    </p>

- **Exit**
    - *Select option `6. Exit` from the menu to close the program safely.* 

</div>

<div style="text-align: center;">

*Enjoy managing your parking spaces efficiently with* **SpotFinder!**

</div style="text-align:center ;">

## Contact


*For any inquiries or contributions, please contact:*

<div style="margin-left: 450px">


- 📧 **Email:** [support@spotfinder.com]
- 📞 **Phone:** [0987 653 4567]
- <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width=15 height=15> **GitHub Profile:** [https://github.com/wilxyz]

</div>
