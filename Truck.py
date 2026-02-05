class Truck:
    max_size = 16
    available = 16
    package_list=[]
    def __init__(self, id, status):
        self.id = id
        self.status = status


    def __str__(self):
        return f"Truck {self.id} {self.status}"
