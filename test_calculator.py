from calculator import Calculator

def test_addition():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"
def test_subtraction():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2, f"Expected 2 but got {result}"
def test_multiplication():
    calc = Calculator()
    result = calc.multiply(4, 3)
    assert result == 12, f"Expected 12 but got {result}"
def test_division():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5, f"Expected 5 but got {result}"
def test_division_by_zero():
    calc = Calculator()
    try:
        calc.divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Denominator cannot be zero.", f"Unexpected error message: {str(e)}"