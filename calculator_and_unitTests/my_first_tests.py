from calculator_and_unitTests.calculator import Calculator, CalculatorError
import pytest

def test_add():
    # arrange
    calc = Calculator()

    # act
    result = calc.add(2, 3)

    # assert
    assert result == 5

def test_sub():
    # arrange
    calc = Calculator()

    # act
    result = calc.sub(9, 3)

    # assert
    assert result == 6

def test_mul():
    # arrange
    calc = Calculator()

    # act
    result = calc.mul(9, 3)

    # assert
    assert result == 27


def test_div():
    # arrange
    calc = Calculator()

    # act
    result = calc.div(9, 3)

    # assert
    assert result == 3


def test_add_weird():
    # arrange
    calc = Calculator()

    # act
    with pytest.raises(CalculatorError):
        result = calc.add("two", 3)

    # assert
    # assert result == 5


def test_add_weirder():
    # arrange
    calc = Calculator()

    # act
    with pytest.raises(CalculatorError):
        result = calc.add("two", "three")

