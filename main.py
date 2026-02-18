import DistanceTable
import Truck
import HashTable
import Package
import datetime
import csv
if __name__ == '__main__':
    distance_table = DistanceTable.DistanceTable('/Users/faridaalakbarli/Downloads/Distance_Table.csv')
    print(distance_table.get_distance(
        "International Peace Gardens\n 1060 Dalton Ave S",
        "Sugar House Park\n 1330 2100 S"))

    hashtable = HashTable.HashTable()
    with open('/Users/faridaalakbarli/Downloads/PackageFile.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            package = Package.Package(int(row[0]), row[1], row[2], row[4],
                                      row[5], row[6], "at hub")
            hashtable.insert(package)

    hashtable.lookup(1)

    truck1 = Truck.Truck(truck_id=1, departure_time=datetime.strptime("08:00", "%H:%M"))
    truck1.load_packages()
    print(distance_table.addresses)