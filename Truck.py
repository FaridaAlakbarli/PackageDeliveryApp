from datetime import time, timedelta


class Truck:


    def __init__(self, truck_id, departure_time):
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.packages = []
        self.current_location = "HUB"
        self.mileage = 0.0
        self.current_time = departure_time


    def load_packages(self, package_id_list):
        if len(package_id_list) < 16:
            self.packages=package_id_list
        else:
            print("Truck is full")


    def travel_to(self, address, distance):
        self.mileage += distance
        travel_seconds = (distance / 18) * 3600
        self.current_time += timedelta(seconds = travel_seconds)
        self.current_location = address


    def deliver_package(self, package_id, hashtable):
        hashtable.update_status(package_id, "Delivered",
                                self.current_time)

        self.packages.remove(package_id)


    def return_to_hub(self, distance):
        self.travel_to("HUB", distance)


    def __str__(self):
        return (f"Truck: {self.truck_id} | "
                f"Mileage: {self.mileage} | "
                f"Location: {self.current_location} | "
                f"Time: {self.current_time}")
