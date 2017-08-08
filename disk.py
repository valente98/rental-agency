import core


def list_of_cars():
    left = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([
            split_string[0], split_string[1], split_string[2],
            float(split_string[3]),
            float(split_string[4])
        ])
    return left


def num_of_car(decision, car):
    str_l = ['i.d num, name_of_car, price, amount_of_car']
    left = list_of_cars()
    for item in left:
        if item == car:
            if int(decision) > int(item[4]):
                return False
            else:
                item[4] = int(item[4]) - int(decision)
        item[3] = str(item[3])
        item[4] = str(item[4])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)
    return True


def help_keep_history(user_name, total, car, decision):
    message = '\n{}, ${}, {}'.format(user_name, car[:3], total, decision)
    with open('history.txt', 'a') as file:
        file.write(message)


def return_inventory(amount, cars, car):
    str_l = ['i.d num, name_of_car, price, amount_of_car']
    for item in cars:
        if item == car:
            item[4] += int(amount)
        item[3] = str(item[3])
        item[4] = str(item[4])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('inventory.txt', 'w') as file:
        file.write(message)