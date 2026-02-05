class Package:
    def __init__(self, id, address, city,
                zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"Package {self.id}"

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

