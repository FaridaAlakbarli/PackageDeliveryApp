#Student ID: 012234998 Student Name: Farida Alakbarli


import DistanceTable
import Truck
import HashTable
import Package
from datetime import *
import csv
import deliver_truck
if __name__ == '__main__':
    #store distance data from csv file
    distance_table = DistanceTable.DistanceTable('/Users/faridaalakbarli/Downloads/Distance_Table.csv')

    #create package instances and insert them into hashtable
    hashtable = HashTable.HashTable()
    with open('/Users/faridaalakbarli/Downloads/PackageFile.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            package = Package.Package(int(row[0]), row[1], row[2], row[4],
                                      row[5], row[6], "at hub")
            hashtable.insert(package)

    #create truck instances and load them with packages
    truck1 = Truck.Truck(truck_id=1, departure_time=datetime.combine(date.today(), time(8, 0)))
    truck1.load_packages([15, 16, 13, 14, 1, 20, 29, 30, 31, 34, 37, 40], hashtable)
    truck2 = Truck.Truck(truck_id=2, departure_time=datetime.combine(date.today(),time(9, 5)))
    truck2.load_packages([6, 25, 2, 3, 10, 18, 21, 26, 27, 28, 32, 33, 36, 38], hashtable)

    #deliver packages
    deliver_truck.deliver_truck(truck1, hashtable, distance_table)
    deliver_truck.deliver_truck(truck2, hashtable, distance_table)

    #modify packages 9 before loading
    package9 = hashtable.lookup(9)
    package9.address = '410 S State St'
    package9.zipcode = '84111'
    hashtable.insert(package9)

    truck3 = Truck.Truck(truck_id=3, departure_time=truck1.current_time)
    truck3.load_packages([4, 5, 7, 8, 9, 11, 12, 17, 19, 22, 23, 24, 35, 39], hashtable)

    deliver_truck.deliver_truck(truck3, hashtable, distance_table)

    #user interface
    print('WGUPS Delivery System')
    while True:
        print("\nMenu:")
        print("1. View all packages at a specific time")
        print("2. View single package by ID")
        print("3. View total mileage")
        print("4. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            input_time = input("Enter time in 12hr format: ")
            user_time = datetime.strptime(input_time, "%I:%M %p")
            new_user_time = user_time.combine(date.today(), time(user_time.hour, user_time.minute))

            #compare user time to delivery and/or departure time of the package
            for bucket in hashtable.table:
                for package in bucket:

                    if new_user_time < package.departure_time:
                        print("At Hub")

                    elif package.departure_time <= new_user_time < package.delivery_time:
                        print("En Route")

                    else:
                        print(f"Delivered at {package.delivery_time.time()}")


        elif choice == "2":
            user_package_id = int(input("Enter package ID to see delivery status: "))
            print(hashtable.lookup(user_package_id).status, " at", hashtable.lookup(user_package_id).delivery_time)
        elif choice == "3":
            print(truck1.mileage + truck2.mileage + truck3.mileage, " miles in total")
        elif choice == "4":
            break
        else:
            print("Invalid option")


