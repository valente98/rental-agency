def set_num_equal_num(picking):
    d = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}
    if picking in d.keys():
        choice = d[picking]
    return choice
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