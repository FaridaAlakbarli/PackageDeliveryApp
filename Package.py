class Package:
    def __init__(self, package_id, address, city, zipcode, deadline, weight, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time=None
        self.departure_time=None

    def __str__(self):
        return (f"ID: {self.id}, Address: {self.address}, City: {self.city},"
                f"Zipcode: {self.zipcode}, Deadline: {self.deadline},"
                f"Weight: {self.weight}, Status: {self.status},"
                f"Delivery time: {self.delivery_time}")