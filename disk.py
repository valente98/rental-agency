def list_of_cars():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], split_string[1], float(split_string[2]), float(split_string[3])])
    return left