import core
import disk
def intro():
    return input('''\n\tWhich car would you like to see?\n 
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
def chosen_car(car, deposit, car_1):
    print('You have chosen',car,'the renting price per day is, $' + str(car_1)+'.')
    print('\nThe deposit of this vihicle will be, $'+str(deposit)+'.')
    return input('''\nWould you like to keep going or would you like to rent this car.\n
    Type in the number of your choice.\n
    \t1. If you would like to rent this car.
    \t2. If you would like to change car.\n''') 

def renting_or_returning():
    print('\n\tWelcome to Valente\'s 2017 Exotic Cars!')
    return input('''Hi! Are you returning a vehicle or renting a vehicle.\n
    Type in the number of your choice.\n
    \t1. I'm renting a vehicle.
    \t2. I'm returning a vehicle.\n''')

def main():
    cars = disk.list_of_cars()
    choice = renting_or_returning()
    if choice == '1' or choice.lower() == 'one':
        picking = intro()
        while picking.lower() != 'q':
            if picking == core.set_num_equal_num(picking):
                user_choice = core.set_num_equal_num(picking)
                car = core.choice_of_car(user_choice, cars)
                deposit = core.replacement(car)   
                car_1 = core.calculate_price_of_renting_with_taxes(car)
                decision = chosen_car(car, deposit, car_1)
                break
            else:
                print('Sorry invalid choice. Please try again.')
            choice = intro()

if __name__ == '__main__':
    main()