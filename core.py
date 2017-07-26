
def choice_of_car(choice,cars):
    for item in cars:
        if item[0].startswith(choice):
            return item[:4]

def calculate_price_of_renting_with_taxes(car):    
    renting = car[3] * .01
    sales_tax = renting * .07
    return renting + sales_tax

def replacement(car):
    return car[3] * .1