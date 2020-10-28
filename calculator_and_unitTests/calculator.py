import numbers


class CalculatorError(Exception):
    pass

class Calculator:

    def __init__(self, printer):
        self.printer = printer


    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a + b
        except TypeError:
                raise CalculatorError()

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f"{operand} not a number")


    def call_calc_printer(self):
        self.printer.persist()
        print("no")