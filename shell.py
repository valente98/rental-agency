import core
import disk
def intro():
    return input('''\nWelcome to Valente's 2017 Exotic Cars! Which car would you like to see?\n 
    Type the number of the choice of your car\n
    \t1. Alfa Romeo 4c Coupe
    \t2. Audi R8 V10 Plus
    \t3. BMW i8
    \t4. Corvette z06
    \t5. Cheverlets Camaro
    \t6. Dodge Challenger
    \t7. Dodge Viper
    \t8. Ford Mustang Shelby GT350R
    \t9. Lamborghini Huracan
    \t10. Porche 911 GT3 RS \n''')

def main():
    cars = disk.list_of_cars()
    choice = intro()
    car = core.choice_of_car(choice, cars)
    print(car)
    car_1 = core.calculate_price_of_renting_with_taxes(car)
    print(car_1)
if __name__ == '__main__':
    main()