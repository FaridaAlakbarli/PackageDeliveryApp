class HashTable:

    def __init__(self):
        self.size = 40
        self.table = []
        self.item_count = 0

        for i in range(0, self.size):
            self.table.append([])


    def hash_function(self, package_id):
        return package_id % self.size

    #create insert method
    def insert(self, package):
        index = self.hash_function(package.id)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i].id == package.id:
                bucket[i] = package
                return
        bucket.append(package)

        #increment number of items after each insert
        self.item_count+=1

        load_factor = self.item_count / self.size

        if load_factor > 0.7:
            self.resize()

    #double the hash table size
    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.item_count = 0

        for bucket in old_table:
            for package in bucket:
                self.insert(package)


    #create lookup function to get package details
    def lookup(self, package_id):
        index = self.hash_function(package_id)
        bucket = self.table[index]

        for package in bucket:
            if package.id == package_id:
                return package

        return None

    #create method to update departure time and status
    def update_departure_time(self, package_id, departure_time):
        package = self.lookup(package_id)
        package.status = "en route"
        package.departure_time = departure_time

    #create method to update status after delivery
    def update_status(self, package_id, status, delivery_time):
        package = self.lookup(package_id)

        if package:
            package.status = status
            package.delivery_time = delivery_time

