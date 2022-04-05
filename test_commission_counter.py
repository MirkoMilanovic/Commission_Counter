import pytest
from commission_counter import get_commission

def test_commission_15():
    assert get_commission('2022-06-10') == 15
    assert get_commission('2022-07-10') == 15
    assert get_commission('2022-08-10') == 15
    assert get_commission('2022-09-10') == 15
    

def test_commission_10():
    assert get_commission('2022-01-10') == 10
    assert get_commission('2022-05-10') == 10
    assert get_commission('2022-10-10') == 10
    assert get_commission('2022-12-10') == 10


def test_commission_incorrect_date():
    assert get_commission('2022-00-10') == 'Incorrect date!'
    assert get_commission('2022-13-10') == 'Incorrect date!'
    assert get_commission('2022-05-00') == 'Incorrect date!'
    assert get_commission('2022-05-32') == 'Incorrect date!'
    assert get_commission('yyyy-05-10') == 'Incorrect date format!'
    assert get_commission('Mirko') == 'Incorrect date format!'
    assert get_commission(2022) == 'Incorrect date format!'