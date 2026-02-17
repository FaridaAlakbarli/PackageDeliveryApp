class HashTable:

    def __init__(self):
        self.size = 53
        self.table = []

        for i in range(0, self.size):
            self.table.append([])


    def hash_function(self, package_id):
        return package_id % self.size


    def insert(self, package):
        index = self.hash_function(package.id)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i].id == package.id:
                bucket[i] = package
                return
        bucket.append(package)


    def lookup(self, package_id):
        index = self.hash_function(package_id)
        bucket = self.table[index]

        for package in bucket:
            if package.id == package_id:
                return package

        return None


    def update_status(self, package_id, status, delivery_time):
        package = self.lookup(package_id)

        if package:
            package.status = status
            package.delivery_time = delivery_time

