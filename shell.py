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
    \t2. If you would like to change car.
    Type Q if you would like to end process\n''') 

def renting_or_returning():
    print('\n\tWelcome to Valente\'s 2017 Exotic Cars!')
    return input('''Hi! Are you returning a vehicle or renting a vehicle.\n
    Type in the number of your choice.\n
    \t1. I'm renting a vehicle.
    \t2. I'm returning a vehicle.\n''')

def quantity(decision):
    if decision == '1' or decision == 'one':
        return input('Great!! How many vehicles of the selected model would you like to rent?\n')
    elif decision =='2' or decision == 'two':
        main()
def day():
    return input('Great! For how many days are you wanting to rent it for?\n')

def total_payment(total):
    print('Great choice of car!! your total price $'+ str(total) +'. Thank you for your time and purchase! Please proceed to one of our employees for all the paper work. Have a nice day.')

def main():
    cars = disk.list_of_cars()
    choice = renting_or_returning()
    if choice == '1' or choice.lower() == 'one':
        picking = intro()
        while picking.lower() != 'q':
            l =['1','2','3','4','5','6','7','8','9','10','one','two','three','four','five','six','seven','eight','nine','ten']
            if picking in l:
                user_choice = core.set_num_equal_num(picking)
                car = core.choice_of_car(user_choice, cars)
                deposit = core.replacement(car)   
                car_1 = core.calculate_price_of_renting_with_taxes(car)
                decision = chosen_car(car, deposit, car_1)
                amount = quantity(decision)
                days = day()
                disk.num_of_car(amount,car)
                total = core.calculate_total_price(car_1, deposit, amount, days)
                total_payment(total)
                # disk.help_keep_history(total, car, amount)
                break
            else:
                print('Sorry invalid choice. Please try again.')
            picking = intro()

if __name__ == '__main__':
    main()