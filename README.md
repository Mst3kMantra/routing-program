# WGUPS Routing Program

## Project Overview

The WGUPS Routing Program is a Python application developed to determine an efficient delivery route for the WGUPS.

The program manages approximately 40 packages that must be delivered throughout Salt Lake City while meeting individual package requirements and delivery deadlines. The program uses a **Nearest Neighbor Algorithm** to determine delivery order and a **Hash Table** to store and retrieve package information efficiently.

The primary objective is to:

* Deliver all 40 packages on time.
* Meet all package-specific delivery requirements.
* Keep each truck's load at or below 16 packages.
* Keep the combined total truck mileage below 140 miles.
* Track package delivery status and delivery time.
* Allow package information to be viewed at a specified time.

---

## Features

The program provides the following functionality:

* Stores package information in a hash table.
* Assigns packages to three delivery trucks.
* Supports truck-specific package requirements.
* Uses the Nearest Neighbor Algorithm to determine delivery order.
* Calculates truck mileage.
* Calculates delivery times using an average speed of 18 mph.
* Tracks package status as:

  * At Hub
  * En Route
  * Delivered
* Records the delivery time for each package.
* Handles the corrected delivery address for package #9 at 10:20 a.m.
* Accounts for packages that are not available until 9:05 a.m.
* Allows package information to be queried by package ID and time.
* Calculates the combined mileage of all trucks.

---

## Technologies Used

* **Python 3**
* **Hash Table**
* **Nearest Neighbor Algorithm**
* Object-oriented programming
* CSV/XLSX data processing
* Git/GitHub

---

## Project Files

A typical project structure is:

```text
WGUPS-Routing-Program/
│
├── main.py
├── package.py
├── truck.py
├── hash_table.py
├── distance.py
├── WGUPS Package File.xlsx
├── WGUPS Distance Table.xlsx
├── requirements.txt
└── README.md
```

### File Descriptions

**main.py**

Contains the primary program logic and user interface. It initializes the package and distance data, creates trucks, runs the delivery routes, and displays delivery information.

**package.py**

Contains the Package class and package attributes such as package ID, address, city, state, ZIP code, deadline, weight, status, and delivery time.

**truck.py**

Contains the Truck class and manages truck information including package assignments, current location, mileage, and delivery time.

**hash_table.py**

Contains the hash table implementation used to store and retrieve package objects using the package ID as the key.

**distance.py**

Contains functionality for retrieving distances between delivery locations.

**requirements.txt**

Contains the external Python dependencies required to run the program.

---

## Algorithm

### Nearest Neighbor Algorithm

The program uses the **Nearest Neighbor Algorithm** to determine the order in which packages are delivered.

The algorithm begins at the WGUPS hub and examines the undelivered packages currently assigned to the truck. It selects the package with the shortest distance from the truck's current location.

After delivering the package, the truck's location is updated. The algorithm then searches the remaining packages again and selects the next closest destination.

This process continues until all packages assigned to the truck have been delivered.

Simplified process:

```text
Start at hub
     ↓
Find nearest undelivered package
     ↓
Travel to package destination
     ↓
Deliver package
     ↓
Update mileage and delivery time
     ↓
Remove package from remaining deliveries
     ↓
Find next nearest package
     ↓
Repeat until all packages are delivered
```

The algorithm has an

