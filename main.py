# Student ID: 012936912, Michael Tran
from Truck import Truck
from Package import Package
import csv
import datetime
from HashTable import HashTable
from Package import Package

# Read csv files
with open("csv/distance_table.csv") as file:
    csv_distance = csv.reader(file)
    csv_distance = list(csv_distance)

with open("csv/package_file.csv") as file1:
    csv_package = csv.reader(file1)
    csv_package = list(csv_package)

with open("csv/address.csv") as file2:
    csv_address = csv.reader(file2)
    csv_address = list(csv_address)

# Function to get address index number
def get_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])

# Get distance from two addresses
def distance(x, y):
    distance = csv_distance[x][y]
    if distance == '':
        distance = csv_distance[y][x]
    
    return float(distance)

# Load packages from csv file into hash table
def load_packages(filename, table):
    with open(filename) as file:
        data = csv.reader(file)
        for package in data:
            pack_ID = int(package[0])
            pack_address = package[1]
            pack_city = package[2]
            pack_state = package[3]
            pack_zip = package[4]
            pack_deadline = package[5]
            pack_weight = package[6]
            pack_status = "Hub"

            unpacked_package = Package(pack_ID, pack_address, pack_city, pack_state, pack_zip, pack_deadline, pack_weight, pack_status)

            table.insert(pack_ID, unpacked_package)



# Create hash table
package_table = HashTable()

# Load hash table with packages from csv file
load_packages("csv/package_file.csv", package_table)

# Manually load packages into trucks to fufill special conditions and to cluster deliveries together
truck1 = Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21], 0.0, datetime.timedelta(hours=8),"4001 South 700 East")

# Truck2 contains package 9 and leaves right as the location mistake is updated by waiting at hub until 10:20 AM
truck2 = Truck([3, 18, 36, 38, 9, 4, 5, 7, 8, 10, 11, 12, 17, 22, 23, 24], 0.0, datetime.timedelta(hours=10, minutes=20), "4001 South 700 East")

# Truck 3 will wait for truck 1 to return
truck3 = Truck([6, 2, 25, 26, 27, 28, 32, 33, 35, 39], 0.0, datetime.timedelta(hours=9, minutes=5), "4001 South 700 East")

# Implemenation of nearest neighbor algorithm to deliver packages
def deliver_packages(truck):
    # Cycle through the list of packages on truck until empty
    while len(truck.packages) > 0:
        next_address = 99999999
        next_package = None
        # Check each distance of each package address to truck location against each other until shortest distance is found
        # and select that as next package
        for package in truck.packages:
            if distance(get_address(truck.location), get_address(package_table.get(package).address)) <= next_address:
                next_address = distance(get_address(truck.location), get_address(package_table.get(package).address))
                next_package = package_table.get(package)
        # Removes the same package from the list
        truck.packages.remove(next_package.pack_ID)
        # Adds mileage driven into the truck.mileage
        truck.mileage += next_address
        # Updates truck's current location to the package it drove to
        truck.location = next_package.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.departure_time

# Function to return to hub for switch
def return_to_hub(truck):
    truck.mileage += distance(get_address(truck.location), 0)
    truck.location = "4001 South 700 East"
    truck.time += datetime.timedelta(hours=distance(get_address(truck.location), 0) / 18)

# Method to fix package address mistakes
def fix_mistake():
    package_table.get(9).update_address("410 S State St", "UT", "Salt Lake City", "84111")

def reset_package():
    package_table.get(9).update_address("300 State St", "UT", "Salt Lake City", "84103")

# Deliver packages for trucks
deliver_packages(truck1)

deliver_packages(truck2)

# Truck 1 returns for driver to switch to Truck 3
return_to_hub(truck1)

# Truck 3 departure time is truck 1's arrival at hub to switch after it is done with deliveries
truck3.departure_time = truck1.time
truck3.time = truck1.time
deliver_packages(truck3)

def main():
    # variable for when pack 9 address gets fixed
    pack9_time = datetime.timedelta(hours=10, minutes=20, seconds= 0)

    # UI for program
    print("Western Governors University Parcel Service (WGUPS) Routing Program")
    print("Mileage of Truck 1:")
    print(truck1.mileage)
    print("Mileage of Truck 2:")
    print(truck2.mileage)
    print("Mileage of Truck 3:")
    print(truck3.mileage)
    print("Total mileage of all trucks:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)
    answer = input("Do you want to search for packages? (y/n)\n")
    while answer == "y":
        try:
            # The user will be asked to enter a time to check packages against
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS\n")
            (h, m, s) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            if convert_timedelta >= pack9_time:
                # Fixes package 9's address if at or past 10:20:00 
                fix_mistake()
            # Query for status of all packages or only one
            second_answer = input("To view the status of one package type 'single'. For all packages please type 'all'.\n")
            if second_answer == "all":
                try:
                    # List status of all packages
                    print(package_table.len())
                    for pack_ID in range(1, package_table.len()+ 1):
                        package = package_table.get(pack_ID)
                        package.update_status(convert_timedelta)
                        print(package)
                    answer = input("Continue searching? (y/n)\n")
                    # Reset state of package 9 incase time checked is before it is updated if continue to search picked
                    reset_package()
                except ValueError:
                    print("Wrong entry. Exiting.")
                    exit()
            elif second_answer == "single":
                try:
                    # Query to input a package ID. Wrong entry will cause the program to quit
                    pack_input = input("Enter the numeric package ID\n")
                    package = package_table.get(int(pack_input))
                    package.update_status(convert_timedelta)
                    print(package)
                    answer = input("Continue searching? (y/n)\n")
                    reset_package()
                except ValueError:
                    print("Wrong entry. Exiting.")
                    exit()
            else:
                print("Wrong entry. Exiting.")
                exit()
        except ValueError:
                    print("Wrong entry. Exiting.")
                    exit()
    print("Exiting.")
    exit()

if __name__ == "__main__":
    main()