from abc import ABC
from math import sin, cos

from utils import CalculatorUtil


class AbsCalculator(ABC):

    @staticmethod
    def value_convertor_float(value) -> float:
        if not isinstance(value, float):
            try:
                value = float(value)
            except:
                raise TypeError
        return value

    def enter_first_value(self):
        value_1 = input("Enter first number: ")
        self.value_1 = cal.calculator.value_convertor_float(value_1)
        return self.value_1

    def enter_second_value(self):
        value_2 = input("Enter second number: ")
        self.value_2 = cal.calculator.value_convertor_float(value_2)
        return self.value_2

    def add(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) + self.value_convertor_float(value_2)

    def minus(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) - self.value_convertor_float(value_2)

    def multiple(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) * self.value_convertor_float(value_2)

    def division(self, dividend, divider) -> float:
        divider = self.value_convertor_float(divider)
        if divider == 0:
            raise ZeroDivisionError
        dividend = self.value_convertor_float(dividend)
        return dividend/divider

    def change(self, value_1, value_2):
        if cal.mod == CalculatorUtil.common_calc or cal.mod == CalculatorUtil.scientific_calc:
            choice = input(f"What do you want to do with this values{CalculatorUtil.choices_for_common_and_scientific()}? ").lower()
        elif cal.mod == CalculatorUtil.accountant_calc:
            choice = input(f"What do you want to do with this values{CalculatorUtil.choices_for_accountant()}? ").lower()
        if choice == CalculatorUtil.add:
            return cal.calculator.add(self.value_1, self.value_2)
        elif choice == CalculatorUtil.minus:
            return cal.calculator.minus(self.value_1, self.value_2)
        elif choice == CalculatorUtil.multiple:
            return cal.calculator.multiple(self.value_1, self.value_2)
        elif choice == CalculatorUtil.division:
            return cal.calculator.division(self.value_1, self.value_2)
        elif choice == CalculatorUtil.sinus and cal.mod == CalculatorUtil.accountant_calc:
            return cal.calculator.sinus(self.value_1, self.value_2)
        elif choice == CalculatorUtil.cosinus and cal.mod == CalculatorUtil.accountant_calc:
            return cal.calculator.cosinus(self.value_1, self.value_2)
        else:
            raise ValueError


class CommonCalculator(AbsCalculator):
    pass


class AccountantCalculator(AbsCalculator):

    def sinus(self, value_1, value_2):
        return sin(value_1), sin(value_2)

    def cosinus(self, value_1, value_2):
        return cos(value_1), cos(value_2)


class ScientificCalculator(AbsCalculator):
    cash = []

    def cashing(self):
        self.cash.append(cal.calculator.change(cal.calculator.enter_first_value(), cal.calculator.enter_second_value()))
        return self.cash


class Calculator:
    calculator = CommonCalculator()

    def __init__(self, status: str):
        if status == CalculatorUtil.status_off:
            print('Включите калькулятор')
            raise ValueError
        elif status == CalculatorUtil.status_on:
            mod = input(f'Выбирите тип калькулятора {CalculatorUtil.models()}: ')
            if mod == CalculatorUtil.accountant_calc:
                self.calculator = AccountantCalculator()
            elif mod == CalculatorUtil.scientific_calc:
                self.calculator = ScientificCalculator()
            else:
                mod = CalculatorUtil.common_calc
            self.mod = mod
        else:
            print("Определитесь")
            raise ValueError

    @classmethod
    def change_mode(cls, mod: str):
        if mod == CalculatorUtil.accountant_calc:
            cls.calculator = AccountantCalculator()
        elif mod == CalculatorUtil.scientific_calc:
            cls.calculator = ScientificCalculator()


if __name__ == '__main__':
    status = input(f'Включить калькулятор, да({CalculatorUtil.status_on}) или нет ({CalculatorUtil.status_off}): ').lower()
    cal = Calculator(status=status)
    if cal.mod == CalculatorUtil.common_calc or cal.mod == CalculatorUtil.accountant_calc:
        print(cal.calculator.change(cal.calculator.enter_first_value(), cal.calculator.enter_second_value()))
    elif cal.mod == CalculatorUtil.scientific_calc:
        print(cal.calculator.cashing())
