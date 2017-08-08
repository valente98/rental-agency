import core


def test_choice_of_car():
    l = [['a', 'b', 'c', 123.5], ['b', 'b', 'c', 123.3]]
    assert core.choice_of_car('a', l) == ['a', 'b', 'c', 123.5]


def test_set_num_equal_num():
    d = {'one': '1', 'two': '2', 'three': '3'}
    assert core.set_num_equal_num('three') == '3'
    assert core.set_num_equal_num('one') == '1'


def test_calculate_price_of_renting_with_taxes():
    car = ['a', 'b', 'c', 12]
    assert core.calculate_price_of_renting_with_taxes(car) == .13


def test_replacement():
    car = ['a', 'b', 'c', 15]
    assert core.replacement(car) == 1.5


def test_calculate_total_price():
    assert core.calculate_total_price(50, 100, 1, 3) == 450


def test_calc_return_depository():
    car = ['a', 'b', 'c', 25]
    assert core.calc_return_depository(car, 3) == 7.5


def test_revenue_history():
    car = [['a', 'b', 'c', 'd', 25, 0], ['a', 'b', 'c', 'd', 25, 2]]
    assert core.revenue_history(car) == 25