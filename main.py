import DistanceTable
if __name__ == '__main__':
    distance_table = DistanceTable.DistanceTable('/Users/faridaalakbarli/Downloads/Distance_Table.csv')
    print(distance_table.get_distance(
        "International Peace Gardens\n 1060 Dalton Ave S",
        "Sugar House Park\n 1330 2100 S"))
    print(distance_table.addresses)