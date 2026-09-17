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
* Git/GitLab

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

The algorithm has an overall time complexity of **O(n²)** because the remaining packages are searched for every delivery.

---

## Data Structure

### Hash Table

The program uses a hash table to store package information.

The **package ID** is used as the key because each package has a unique ID.

For example:

```text
Package ID → Package Information
     1     → Address, deadline, weight, status, delivery time
     2     → Address, deadline, weight, status, delivery time
     3     → Address, deadline, weight, status, delivery time
```

The hash table allows package information to be retrieved and updated efficiently.

Average-case complexity:

| Operation | Complexity |
| --------- | ---------- |
| Insert    | O(1)       |
| Search    | O(1)       |
| Update    | O(1)       |
| Delete    | O(1)       |

---

## Package Constraints

The program accounts for the package restrictions provided in the WGUPS scenario.

### Truck Capacity

Each truck can carry a maximum of 16 packages.

### Truck Restrictions

Packages with truck-specific requirements are assigned to the appropriate truck before the delivery route begins.

### Delayed Packages

Packages that are unavailable until 9:05 a.m. remain at the hub until they become available.

### Package #9

Package #9 initially has an incorrect delivery address.

The address is corrected at 10:20 a.m. to:

```text
410 S. State St.
Salt Lake City, UT 84111
```

The program updates the package information before the package is delivered.

### Truck Speed

The trucks travel at an average speed of:

```text
18 miles per hour
```

Travel time is calculated using:

```text
Travel Time = Distance / Speed
```

---

## Package Status

The program tracks the status of every package.

Possible statuses include:

```text
At Hub
En Route
Delivered
```

When a package is delivered, its delivery time is recorded.

Example:

```text
Package ID: 15
Status: Delivered
Delivery Time: 9:35 AM
```

This allows the supervisor to determine the status of a package at a specific point during the delivery day.

---

## Running the Program

### Requirements

Before running the application, install:

* Python 3
* Git
* GitLab account/repository

If a virtual environment is used, create one with:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

From the project directory, run:

```bash
python main.py
```

The program will load the package and distance information and begin the routing process.

After the routes have been calculated, the program can display package delivery information and total truck mileage.

---

## Example Output

An example of the expected output format is:

```text
WGUPS Routing Program

Package ID: 1
Address: 195 W Oakland Ave
City: Salt Lake City
State: UT
ZIP: 84115
Deadline: 10:30 AM
Status: Delivered
Delivery Time: 8:45 AM
```

The program also reports the total distance traveled by the trucks:

```text
Truck 1 Mileage: XX.XX miles
Truck 2 Mileage: XX.XX miles
Truck 3 Mileage: XX.XX miles

Total Mileage: XX.XX miles
```

The final solution should have all 40 packages delivered on time and maintain a combined truck mileage below 140 miles.

---

## Complexity

The primary routing algorithm has a time complexity of:

```text
O(n²)
```

This occurs because the program searches the remaining packages to identify the nearest destination after each delivery.

The hash table provides average-case:

```text
O(1)
```

lookup, insertion, and update operations.

The overall space complexity of the program is:

```text
O(n)
```

because package records and associated delivery information are stored in memory.

---

## Design Considerations

The program separates package data, truck information, distance information, and routing logic into separate components. This modular design makes the program easier to understand, test, and maintain.

The hash table provides efficient access to package information, while the Nearest Neighbor Algorithm provides a straightforward method for determining delivery order.

The design can also be adapted to additional packages and delivery locations by expanding the package and distance data without fundamentally changing the routing process.

---

## Data Sources

The following files were provided for the WGUPS Routing Program:

* WGUPS Package File
* WGUPS Distance Table
* Salt Lake City Downtown Map

These files provide the package requirements, delivery locations, and distances necessary for the routing application.

---

## Author

**Michael Tran**
