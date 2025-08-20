# Smart-Parking-Lot-Management
 Smart Parking Lot Management System (Python)
 Project Overview

This project is a console-based Parking Lot Management System implemented in Python.
It simulates a smart parking system where cars can enter (park) and exit (leave). The parking lot uses a Linked List data structure to dynamically allocate slots for cars.

The project demonstrates:

Entry and Exit tracking

Linked List for parked cars

Dynamic Memory Allocation for parking slots (each car is stored as a new node)

Overflow Handling when the parking lot is full

 Features

 Park a car with its unique number

 Remove (exit) a car by its number

 Display all currently parked cars with their slot numbers

 Prevents adding cars when the parking is full

 Handles attempts to remove cars that are not in the lot

 Uses Linked List nodes to simulate dynamic slot allocation

 How It Works

Each car is represented as a node in a linked list.

New cars are dynamically added (like memory allocation).

Removing a car frees the slot (node deletion).

The system keeps track of capacity, so no more cars can enter when full.

 How to Run

Clone this repository:

git clone https://github.com/your-username/smart-parking-lot.git
cd smart-parking-lot


Run the Python file:

python parking_lot.py


Use the menu options to interact with the system:

1 → Park Car

2 → Remove Car

3 → View Parking Lot

4 → Exit

Example Output
1. Park Car
2. Remove Car
3. View Parking Lot
4. Exit
Enter choice: 1
Enter Car Number: MH12AB1234
 Car MH12AB1234 parked successfully.

1. Park Car
2. Remove Car
3. View Parking Lot
4. Exit
Enter choice: 1
Enter Car Number: DL05CD4321
 Car DL05CD4321 parked successfully.

1. Park Car
2. Remove Car
3. View Parking Lot
4. Exit
Enter choice: 1
Enter Car Number: KA09MN0001
 Car KA09MN0001 parked successfully.

1. Park Car
2. Remove Car
3. View Parking Lot
4. Exit
Enter choice: 1
Enter Car Number: GJ18PQ7890
 Parking Full! Car GJ18PQ7890 cannot be parked.

Enter choice: 3
 Cars currently parked:
Slot 1: Car MH12AB1234
Slot 2: Car DL05CD4321
Slot 3: Car KA09MN0001

Enter choice: 2
Enter Car Number to Remove: DL05CD4321
 Car DL05CD4321 exited.

Enter choice: 3
 Cars currently parked:
Slot 1: Car MH12AB1234
Slot 2: Car KA09MN0001

Enter choice: 4
Exiting Parking System...

 Tech Stack

Language: Python 3

Data Structure: Linked List

🚀 Future Improvements

Add automatic nearest slot allocation (like real parking systems).

Add timestamps for parked cars.

Add fees calculation based on parking duration.

Add GUI (Tkinter / PyQt) for better user interaction.
