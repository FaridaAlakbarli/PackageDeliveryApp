class Package:
    def __init__(self, id, address, deadline,
                 city, zipcode, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = status

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

