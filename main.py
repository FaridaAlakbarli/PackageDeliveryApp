import csv
import Package
import Truck
if __name__ == '__main__':
    packageDictionary = {}
    with open('/Users/faridaalakbarli/Downloads/PackageFile.csv') as csv_file:
        csv_reader=csv.reader(csv_file)
        for row in csv_reader:
            package = Package.Package(row[0], row[1], row[2], row[4], row[5], row[6], row[6])
            packageDictionary[package.get_id()] = package


    truck_1 = Truck.Truck(1, "at_hub")
    for package in packageDictionary:
        if packageDictionary[package].deadline!="EOD" and truck_1.available>0:
            truck_1.package_list.append(packageDictionary[package])
            truck_1.available-=1

    truck_2 = Truck.Truck(2, "at_hub")
    print(truck_1.available)
    print(len(truck_1.package_list))

