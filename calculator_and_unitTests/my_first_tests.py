from calculator_and_unitTests.calculator import Calculator, CalculatorError
from calculator_and_unitTests.calc_printer import calc_printer
import pytest

from mock import Mock


# def test_add():
#     # arrange
#     calc = Calculator()
#
#     # act
#     result = calc.add(2, 3)
#
#     # assert
#     assert result == 5
#
#
# def test_sub():
#     # arrange
#     calc = Calculator()
#
#     # act
#     result = calc.sub(9, 3)
#
#     # assert
#     assert result == 6
#
#
# def test_mul():
#     # arrange
#     calc = Calculator()
#
#     # act
#     result = calc.mul(9, 3)
#
#     # assert
#     assert result == 27
#
#
# def test_div():
#     # arrange
#     calc = Calculator()
#
#     # act
#     result = calc.div(9, 3)
#
#     # assert
#     assert result == 3
#     assert True
#
#
# def test_add_weird():
#     # arrange
#     calc = Calculator()
#
#     # act
#     with pytest.raises(CalculatorError):
#         result = calc.add("two", 3)
#
#     # assert
#     # assert result == 5
#
#
# def test_add_weirder():
#     # arrange
#     calc = Calculator()
#
#     # act
#     with pytest.raises(CalculatorError):
#         result = calc.add("two", "three")

#
# @pytest.fixture
# def input_value():
#     input = 6
#     return input
#
#
# def test_divisible_by_3(input_value):
#     assert input_value % 3 == 0
#
#
# def test_divisible_by_6(input_value):
#     assert input_value % 6 == 0
#
#
# @pytest.mark.parametrize("input, output", [(1, 1), (2, 2), (3, 3)])
# def test_paramterized(input, output):
#     assert input == output


@pytest.fixture
def mock_calc():

    return Mock(spec=calc_printer)

def test_printer_method_is_called(mock_calc):
    calc = Calculator(mock_calc)

    calc.call_calc_printer()

    mock_calc.persist.assert_called_with()




