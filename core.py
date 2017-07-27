def set_num_equal_num(choice):
    if choice == '1' or choice.lower() == 'one':
        return '1'
    elif choice == '2' or choice.lower() == 'two':
        return '2'
    elif choice == '3' or choice.lower() == 'three':
        return '3'
    elif choice == '4' or choice.lower() == 'four':
        return '4'
    elif choice == '5' or choice.lower() == 'five':
        return '5'
    elif choice == '6' or choice.lower() == 'six':
        return '6'
    elif choice == '7' or choice.lower() == 'seven':
        return '7'
    elif choice == '8' or choice.lower() == 'eight':
        return '8'
    elif choice == '9' or choice.lower() == 'nine':
        return '9' 
    elif choice == '10' or choice.lower() == 'ten':
        return '10'  

def choice_of_car(user_choice,cars):
    for item in cars:
        if item[0].startswith(user_choice):
            return item[:4]

def calculate_price_of_renting_with_taxes(car):    
    renting = car[3] * .01
    sales_tax = renting * .07
    return renting + sales_tax

def replacement(car):
    return car[3] * .1