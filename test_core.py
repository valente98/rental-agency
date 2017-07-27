import core
def test_choice_of_car():
    l = [
        ['a','b','c',123.5],
        ['b','b','c',123.3]
        ]
    assert core.choice_of_car('a',l) == ['a','b','c',123.5]