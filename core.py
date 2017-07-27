def set_num_equal_num(picking):
    if picking == '1' or picking.lower() == 'one':
        return '1'
    elif picking == '2' or picking.lower() == 'two':
        return '2'
    elif picking == '3' or picking.lower() == 'three':
        return '3'
    elif picking == '4' or picking.lower() == 'four':
        return '4'
    elif picking == '5' or picking.lower() == 'five':
        return '5'
    elif picking == '6' or picking.lower() == 'six':
        return '6'
    elif picking == '7' or picking.lower() == 'seven':
        return '7'
    elif picking == '8' or picking.lower() == 'eight':
        return '8'
    elif picking == '9' or picking.lower() == 'nine':
        return '9' 
    elif picking == '10' or picking.lower() == 'ten':
        return '10'  

def choice_of_car(user_choice,cars):
    for item in cars:
        if item[0].startswith(user_choice):
            return item[:4]

def calculate_price_of_renting_with_taxes(car):    
    renting = car[3] * .01
    sales_tax = renting * .07
    return round((renting + sales_tax), 2)

def replacement(car):
    return car[3] * .1