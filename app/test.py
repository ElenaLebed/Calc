import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self,2,4) == 8

    def test_division(self):
        assert self.calc.division(self,20,2) == 10

    def test_subtraction(self):
        assert self.calc.subtraction(self,17,5) == 12

    def test_adding(self):
        assert self.calc.adding(self,13,8) == 21

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')