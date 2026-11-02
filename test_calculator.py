
import pytest
from calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(10, 5) == 15

def test_subtract():
    assert calc.subtract(10, 5) == 5

def test_multiply():
    assert calc.multiply(10, 5) == 50

def test_divide():
    assert calc.divide(10, 5) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
