import Truck
import HashTable
import DistanceTable
from datetime import *

def deliver_truck(truck, hash_table, distance_table):
    while truck.packages:
        closest_distance = float("inf")
        closest_package_id = None
        closest_address = None

        earliest_deadline = None
        for package_id in truck.packages:
            package = hash_table.lookup(package_id)
            deadline_string = package.deadline

            if package.deadline != "EOD":
                package_deadline = datetime.strptime(deadline_string, "%I:%M %p").time()
                if earliest_deadline is None or package_deadline < earliest_deadline:
                    earliest_deadline = package_deadline

        priority_packages = []

        if earliest_deadline is not None:
            for package_id in truck.packages:
                package = hash_table.lookup(package_id)
                if package.deadline != "EOD":
                    package_deadline = datetime.strptime(
                        package.deadline, "%I:%M %p"
                    ).time()
                    if package_deadline == earliest_deadline:
                        priority_packages.append(package_id)
        else:
            priority_packages = truck.packages


        for package_id in priority_packages:
            package = hash_table.lookup(package_id)
            package_address = package.address

            distance = distance_table.get_distance(truck.current_location, package_address)

            if distance < closest_distance:
                closest_distance = distance
                closest_package_id = package_id
                closest_address = package_address

        truck.travel_to(closest_address, closest_distance)

        packages_to_deliver = []

        for package_id in truck.packages:
            package = hash_table.lookup(package_id)
            if package.address == closest_address:
                packages_to_deliver.append(package_id)

        for package_id in packages_to_deliver:
            truck.deliver_package(package_id, hash_table)


    distance_back = distance_table.get_distance(truck.current_location, "HUB")

    truck.travel_to("HUB", distance_back)


