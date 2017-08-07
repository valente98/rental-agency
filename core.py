def set_num_equal_num(picking):
    ''' string -> string 
    takes in a string and returns the variable string of it
    
    >>> set_num_equal_num('one')
    '1'
    >>> set_num_equal_num('two')
    '2'
    >>> set_num_equal_num('three')
    '3'
    '''
    d = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}
    if picking in d.keys():
        picking = d[picking]
    return picking
def choice_of_car(user_choice,cars):
    '''(string, list) -> list
    takes in a list and a string and returns the list that starts with the string
    >>> choice_of_car('1', [['1', 'b', 'c']])
    ['1', 'b', 'c']
    '''
    for item in cars:
        if item[0].startswith(user_choice):
            return item

def calculate_price_of_renting_with_taxes(car):
    '''list -> float
    takes a list and return the float of the total price
    >>> calculate_price_of_renting_with_taxes(['a', 'b', 'c', 20])
    0.21
    '''    
    renting = car[3] * .01
    sales_tax = renting * .07
    return round((renting + sales_tax), 2)

def replacement(car):
    '''list -> float

    takes a list and returns a the float number of the deposit
    
    >>> replacement(['a', 'b', 'c', 100])
    10.0
    '''
    return car[3] * .1

def calculate_total_price(car_1, deposit, decision, days):
    '''(float, float, int, int) -> float

    return the float of the total price

    >>> calculate_total_price(12.33, 12.33, 1, 2)
    49.32
    '''
    return round((((car_1 + deposit) * int(decision)) * int(days)), 2)

def calc_return_depository(car, amount):
    '''(list, float) -> float

    return the float of the deposit to return it
     
    >>> calc_return_depository(['a', 'b', 'c', 300], 2)
    60.0
    '''
    return round((float(car[3]) * .1) * float(amount), 2)