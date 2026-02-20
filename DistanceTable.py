import csv

class DistanceTable:
    def __init__(self, filename):
        self.addresses = ['HUB']
        self.distances = []
        self.load_csv(filename)

    def load_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader= csv.reader(csvfile)

            for row_index, row in enumerate(reader):
                if row_index == 0:
                    for address in row[3:]:
                        self.addresses.append(address.split('\n')[-1].strip())
                else:
                    self.distances.append(row[2:])

    def get_address_index(self, address):
        return self.addresses.index(address)

    def get_distance(self, address_1, address_2):
        index_1 = self.get_address_index(address_1)
        index_2 = self.get_address_index(address_2)

        distance = self.distances[index_1][index_2]

        if distance == '':
            distance = self.distances[index_2][index_1]

        return float(distance)