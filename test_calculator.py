import unittest
from utils import CalculatorUtil
from main import Calculator


class TestCalculator(unittest.TestCase):
    def test_status(self):
        print('\ntest_status: ')
        self.status = CalculatorUtil.status_on
        self.assertEqual(self.status, CalculatorUtil.status_on)

    def test_status1(self):
        print('\ntest_status: ')
        self.status = CalculatorUtil.status_off
        self.assertEqual(self.status, CalculatorUtil.status_off)
        self.assertRaises(ValueError)

    @classmethod
    def setUpClass(cls):
        print(f"setUpClass\n{'='*50}")
        cls.calculator = Calculator(CalculatorUtil.status_on)

    def setUp(self):
        print(f"\n{'-'*50}\nsetUp")

    def tearDown(self):
        print(f"tearDown")

    @classmethod
    def tearDownClass(cls):
        print(f"\n{'='*50}\ntearDownClass")

    def test_add(self):
        print('\ntest_add: ')
        value1 = 2
        value2 = 4
        res = 6
        self.assertEqual(self.calculator.add(value1, value2), res)

    def test_add_not_eq(self):
        print('\ntest_add: ')
        value1 = 2
        value2 = 4
        res = 7
        self.assertNotEqual(self.calculator.add(value1, value2), res)

    def test_add_1(self):
        print('\ntest_add: ')
        calc_response = self.calculator.add(3, 7)
        print('calc_response: ', calc_response)
        expactation = 10
        print('expactation: ', expactation)
        self.assertEqual(calc_response, expactation)

    def test_subtract(self):
        print('\ntest_subtract: ')
        self.assertEqual(5, self.calculator.minus(10, 5))

    def test_multiply(self):
        print('\ntest_multiply: ')
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        print('\ntest_divide: ')
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_divide_on_zero(self):
        print('\ntest_divide_zero: ')
        self.assertEqual(self.calculator.division(10, 0), 'infinity')
        self.assertRaises(ZeroDivisionError)

    def test_divide_zero(self):
        print('\ntest_divide_zero: ')
        self.assertEqual(self.calculator.division(0, 10), 0)

    def test_value_convertor_float(self):
        print('\ntest_value_convertor_float: ')
        self.assertEqual(self.value_convertor_float(3), 3.0)

    def test_value_convertor_float1(self):
        print('\ntest_value_convertor_float: ')
        self.assertEqual(self.value_convertor_float(3.0), 3.0)

    def test_value_convertor_float2(self):
        print('\ntest_value_convertor_float: ')
        self.assertEqual(self.value_convertor_float("3"), 3.0)

    def test_value_convertor_float_not_eq(self):
        print('\ntest_value_convertor_float: ')
        self.assertNotEqual(self.value_convertor_float("three"), 3.0)
