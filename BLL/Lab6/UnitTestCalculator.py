import unittest

from BLL.Lab2.Calculator import Calculator


class UnitTestsCalculator(unittest.TestCase):
    def setUp(self):
        # This method is called before each test. It sets up the Calculator object for testing.
        self.calculator = Calculator()

    def test_add(self):
        # This test checks if the addition operation works correctly.
        first_input = float(5)
        second_input = float(3)
        operator = '+'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(8))
        print("Added successful")

    def test_subtract(self):
        # This test checks if the subtraction operation works correctly.
        first_input = float(5)
        second_input = float(3)
        operator = '-'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(2))
        print("Subtracted successful")

    def test_multiply(self):
        # This test checks if the multiplication operation works correctly.
        first_input = float(5)
        second_input = float(3)
        operator = '*'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(15))
        print("Multiplied successful")

    def test_divide(self):
        # This test checks if the division operation works correctly.
        first_input = float(6)
        second_input = float(3)
        operator = '/'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(2))
        print("Divided successful")

    def test_square_root(self):
        # This test checks if the square root operation works correctly.
        first_input = float(9)
        second_input = float(0)
        operator = '√'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(3))
        print("Square root get successful")

    def test_power(self):
        # This test checks if the power operation works correctly.
        first_input = float(-2)
        second_input = float(2)
        operator = '^'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(4))
        print("Power successful")

    def test_leftover(self):
        # This test checks if the modulo operation works correctly.
        first_input = float(10)
        second_input = float(3)
        operator = '%'
        self.assertEqual(self.calculator.calculate(first_input, operator, second_input), float(1))
        print("Leftover successful")

    def test_divide_by_zero(self):
        # This test checks if the Calculator correctly handles division by zero.
        first_input = float(5)
        second_input = float(0)
        operator = '/'
        self.assertIsNone(self.calculator.calculate(first_input, operator, second_input))

    def test_square_root_of_negative(self):
        # This test checks if the Calculator correctly handles square root of a negative number.
        first_input = float(-9)
        second_input = float(0)
        operator = '√'
        self.assertIsNone(self.calculator.calculate(first_input, operator, second_input))

