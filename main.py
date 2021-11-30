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
        self.value_1 = cal.calculator.value_convertor_float(input("Enter first number: "))
        return self.value_1

    def enter_second_value(self):
        self.value_2 = cal.calculator.value_convertor_float(input("Enter second number: "))
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
        if cal.mod == CalculatorUtil.common_calc:
            choice = input(f"What do you want to do with this values{CalculatorUtil.choices_for_common()}? ").lower()
        elif cal.mod == CalculatorUtil.accountant_calc:
            choice = input(f"What do you want to do with this values{CalculatorUtil.choices_for_accountant()}? ").lower()
        elif cal.mod == CalculatorUtil.scientific_calc:
            choice = input(f"What do you want to do with this values{CalculatorUtil.choices_for_scientific()}? ").lower()
        if choice == CalculatorUtil.add:
            return cal.calculator.add(value_1, value_2)
        elif choice == CalculatorUtil.minus:
            return cal.calculator.minus(value_1, value_2)
        elif choice == CalculatorUtil.multiple:
            return cal.calculator.multiple(value_1, value_2)
        elif choice == CalculatorUtil.division:
            return cal.calculator.division(value_1, value_2)
        elif choice == CalculatorUtil.sinus and cal.mod == CalculatorUtil.accountant_calc:
            return cal.calculator.sinus(value_1, value_2)
        elif choice == CalculatorUtil.cosinus and cal.mod == CalculatorUtil.accountant_calc:
            return cal.calculator.cosinus(value_1, value_2)
        elif choice == CalculatorUtil.sqr and (cal.mod == CalculatorUtil.scientific_calc or CalculatorUtil.common_calc):
            return cal.calculator.sqr(value_1, value_2)
        elif choice == CalculatorUtil.sqrt and (cal.mod == CalculatorUtil.scientific_calc or CalculatorUtil.common_calc):
            return cal.calculator.sqrt(value_1, value_2)
        else:
            raise ValueError


class CommonCalculator(AbsCalculator):

    def sqr(self, value_1, value_2) -> float:
        return value_1 ** value_2

    def sqrt(self, value_1, value_2) -> float:
        if value_1 > 0:
            return round(value_1 ** (1/value_2), 2)
        else:
            raise ValueError


class AccountantCalculator(AbsCalculator):
    cash = []

    def cashing(self):
        self.cash.append(cal.calculator.change(cal.calculator.enter_first_value(), cal.calculator.enter_second_value()))
        return self.cash


class ScientificCalculator(CommonCalculator, AccountantCalculator):
    def sinus(self, value_1) -> float:
        return sin(value_1)

    def cosinus(self, value_1) -> float:
        return cos(value_1)


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
    if cal.mod == CalculatorUtil.common_calc:
        print(cal.calculator.change(cal.calculator.enter_first_value(), cal.calculator.enter_second_value()))
    elif cal.mod == CalculatorUtil.accountant_calc:
        print(cal.calculator.cashing())
    elif cal.mod == CalculatorUtil.scientific_calc:
        print(cal.calculator.cashing())
