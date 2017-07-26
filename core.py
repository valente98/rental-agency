def choice_of_car(choice,cars):
    for item in cars:
        if item[0].startswith(choice):
            return item
