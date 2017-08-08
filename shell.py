import core
import disk


def intro():
    msg = '''\n\tWhich car would you like to see?\n 
    Type the number of the choice of your car\n
    \t1. Alfa Romeo 4c Coupe\n
    \t2. Audi R8 V10 Plus\n
    \t3. BMW i8\n
    \t4. Corvette z06\n
    \t5. Cheverlets Camaro\n
    \t6. Dodge Challenger\n
    \t7. Dodge Viper\n
    \t8. Ford Mustang Shelby GT350R\n
    \t9. Lamborghini Huracan\n
    \t10. Porche 911 GT3 RS \n
    type Q to quit the process\n'''
    while True:
        picking = input(msg)
        l = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'one', 'two',
            'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'
        ]
        if picking in l:
            return picking
        elif picking.lower() == 'q':
            exit()
        else:
            print('error')
            continue


def chosen_car(car, deposit, car_1):
    print('You have chosen', car,
          'the renting price per day is, $' + str(car_1) + '.')
    print('\nThe deposit of this vihicle will be, $' + str(deposit) + '.')
    msg = '''\nWould you like to keep going or would you like to rent this car.\n
    Type in the number of your choice.\n
    \t1. If you would like to rent this car.
    \t2. If you would like to change car.
    Type Q if you would like to end process\n'''
    while True:
        decision = input(msg)
        if decision == '1' or decision == 'one':
            return input(
                'Great!! How many vehicles of the selected model would you like to rent?\n'
            )
        elif decision == '2' or decision == 'two':
            picking = intro()
        elif decision.lower() == 'q':
            exit()
        else:
            print('Sorry invalid choice.')


def name():
    print('\n\tWelcome to Valente\'s 2017 Exotic Cars!')
    msg = 'Hi, welcome to valente\'s 2017 Exotic Cars. what is your name? '
    return input(msg)


def renting_or_returning():
    msg = '''Hi! Are you returning a vehicle or renting a vehicle.\n
    Type in the number of your choice.\n
    \t1. I'm renting a vehicle.
    \t2. I'm returning a vehicle.\n'''
    while True:
        choice = input(msg).lower()
        if choice in ['1', 'one', 'two', '2']:
            return choice
        else:
            print('error, choose correctly')


def day():
    return input('Great! For how many days are you wanting to rent it for?\n')


def total_payment(total):
    print(
        'Great choice of car!! your total price $' + str(total) +
        '. Thank you for your time and purchase! Please proceed to one of our employees for all the paper work. Have a nice day.'
    )


def return_intro():
    return input('''\nWhich car was the car you have rented?\n 
    Type the number of the choice of your car\n
    \t1. Alfa Romeo 4c Coupe\n
    \t2. Audi R8 V10 Plus\n
    \t3. BMW i8\n
    \t4. Corvette z06\n
    \t5. Cheverlets Camaro\n
    \t6. Dodge Challenger\n
    \t7. Dodge Viper\n
    \t8. Ford Mustang Shelby GT350R\n
    \t9. Lamborghini Huracan\n
    \t10. Porche 911 GT3 RS \n
    type Q to quit the process\n''')


def return_amount():
    return input('Great! How many cars are you returning?\n')


def returning_deposit(depository):
    print('Ok. Since you return the car your returning deposit money wil be $'
          + str(depository))
    print('Thanks for renting a car with us. Have a good day.')


def main():
    cars = disk.list_of_cars()
    user_name = name()
    choice = renting_or_returning()
    if choice == '1' or choice == 'one':
        while True:
            picking = intro()
            user_choice = core.set_num_equal_num(picking)
            car = core.choice_of_car(user_choice, cars)
            deposit = core.replacement(car)
            car_1 = core.calculate_price_of_renting_with_taxes(car)
            decision = chosen_car(car, deposit, car_1)
            if not decision:
                break
            days = day()
            disk.num_of_car(decision, car)
            total = core.calculate_total_price(car_1, deposit, decision, days)
            total_payment(total)
            disk.help_keep_history(user_name, total, car, decision)
            exit()
    elif choice == '2' or choice == '2':
        while True:
            picking = return_intro()
            l = [
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'one',
                'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten'
            ]
            if picking in l:
                user_choice = core.set_num_equal_num(picking)
                car = core.choice_of_car(user_choice, cars)
                deposit = core.replacement(car)
                amount = return_amount()
                disk.return_inventory(amount, cars, car)
                depository = core.calc_return_depository(car, amount)
                returning_deposit(depository)
                exit()
            else:
                print('Sorry invalid choice.')


if __name__ == '__main__':
    main()