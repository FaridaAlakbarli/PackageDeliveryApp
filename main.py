import DistanceTable
import Truck
import HashTable
import Package
from datetime import *
import csv
import deliver_truck
if __name__ == '__main__':
    distance_table = DistanceTable.DistanceTable('/Users/faridaalakbarli/Downloads/Distance_Table.csv')
    '''print(distance_table.get_distance(
        "1060 Dalton Ave S",
        "1330 2100 S"))'''

    hashtable = HashTable.HashTable()
    with open('/Users/faridaalakbarli/Downloads/PackageFile.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            package = Package.Package(int(row[0]), row[1], row[2], row[4],
                                      row[5], row[6], "at hub")
            hashtable.insert(package)

    print(hashtable.lookup(1))

    truck1 = Truck.Truck(truck_id=1, departure_time=datetime.strptime("08:00", "%H:%M"))
    truck1.load_packages([15, 16, 13, 14, 1, 20, 29, 30, 31, 34, 37, 40])
    truck2 = Truck.Truck(truck_id=2, departure_time=datetime.strptime("09:05", "%H:%M"))
    truck2.load_packages([6, 25, 2, 3, 10, 18, 21, 26, 27, 28, 32, 33, 36, 38])

    package9 = hashtable.lookup(9)
    package9.address = '410 S State St'
    hashtable.insert(package9)

    truck3 = Truck.Truck(truck_id=3, departure_time=datetime.strptime("12:00", "%H:%M"))
    truck3.load_packages([4, 5, 7, 8, 9, 11, 12, 17, 19, 22, 23, 24, 35, 39])
    deliver_truck.deliver_truck(truck1, hashtable, distance_table)
    deliver_truck.deliver_truck(truck2, hashtable, distance_table)
    deliver_truck.deliver_truck(truck3, hashtable, distance_table)
    print(truck1.current_time)
    print(truck2.departure_time)
    print(truck3.current_time)
    print(truck1.mileage + truck2.mileage + truck3.mileage)
    print(distance_table.addresses)
    print(hashtable.lookup(6))
