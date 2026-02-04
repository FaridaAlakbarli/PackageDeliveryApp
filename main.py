import csv
import Package
if __name__ == '__main__':
    packageDictionary = {}
    with open('/Users/faridaalakbarli/Downloads/PackageFile.csv') as csv_file:
        csv_reader=csv.reader(csv_file)
        for row in csv_reader:
            package = Package.Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            packageDictionary[package.get_id()] = package

    print(packageDictionary.keys())




