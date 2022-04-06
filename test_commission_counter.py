import pytest
from commission_counter import get_commission

def test_commission_15():
    assert get_commission('2022-06-10', 'airbnb') == 15
    assert get_commission('2022-07-10', 'airbnb') == 15
    assert get_commission('2022-08-10', 'airbnb') == 15
    assert get_commission('2022-09-10', 'airbnb') == 15
    assert get_commission('10 June, 2022', 'bcom') == 15
    assert get_commission('10 July, 2022', 'bcom') == 15
    assert get_commission('10 August, 2022', 'bcom') == 15
    assert get_commission('10 September, 2022', 'bcom') == 15

    assert get_commission('2022-05-10', 'airbnb') == 10
    assert get_commission('2022-10-10', 'airbnb') == 10
    assert get_commission('10 May, 2022', 'bcom') == 10
    assert get_commission('10 October, 2022', 'bcom') == 10

    assert get_commission('2022-01-10', 'airbnb') == 12
    assert get_commission('10 January, 2022', 'bcom') == 12

    assert get_commission('2022-12-10', 'airbnb') == 11
    assert get_commission('10 December, 2022', 'bcom') == 11


def test_commission_incorrect_date():
    assert get_commission('2022-00-10', 'airbnb') == 'Incorrect date format!'
    assert get_commission('2022-13-10', 'airbnb') == 'Incorrect date format!'
    assert get_commission('2022-05-00', 'airbnb') == 'Incorrect date format!'
    assert get_commission('2022-05-32', 'airbnb') == 'Incorrect date format!'
    assert get_commission('yyyy-05-10', 'airbnb') == 'Incorrect date format!'
    assert get_commission('10 Decemberrr, 2022', 'bcom') == 'Incorrect date format!'
    assert get_commission('55 December, 2022', 'bcom') == 'Incorrect date format!'


def test_commission_incorrect_platform():
    assert get_commission('2022-01-10', 'xyz') == 'Incorrect platform!'
    assert get_commission('10 January, 2022', 123) == 'Incorrect platform!'