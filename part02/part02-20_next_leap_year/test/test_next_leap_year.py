import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.next_leap_year'

@points('2.next_leap_year')
class NextLeapYearTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["4321"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_2019(self):
        with patch('builtins.input', side_effect= ["2019", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            expected = 'The next leap year after 2019 is 2020'
            self.assertFalse(len(output) == 0 , f"With the input 2019 your program should print out\n{expected}\nnow your program did not print out anything" )
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n2019your program should print out\n{expected}\nyour program printed out\n{output}" )

    def test_2020(self):
        with patch('builtins.input', side_effect= ["2020", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()

            self.assertFalse(len(output) == 0 , f"Your program did not print out anything with the input 2024" )
            expected = 'The next leap year after 2020 is 2024'
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n2020\1your program should print out\n{expected}\nyour program printed out\n{output}" )

    def test_1896(self):
        with patch('builtins.input', side_effect= ["1896", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()

            self.assertFalse(len(output) == 0 , f"Your program did not print out anything with the input 1896" )

            expected = 'The next leap year after 1896 is 1904'
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n1896\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    def test_divisible_by_four(self):
        values = "4 16 1204 1616 1976 2008".split(" ")
        for value in values:
            acual_value = int(value) - 3
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()
                expected = f'The next leap year after {acual_value} is {acual_value+3}'
                self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{acual_value}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    def test_divisible_by_hundred_not_four_hundred(self):
        values = "500 700 1100 1300 1900".split(" ")
        for value in values:
            acual_value = int(value) - 2
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()
                expected = f'The next leap year after {acual_value} is {acual_value+6}'
                self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{acual_value}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    def test_divisible_by_four_hundred(self):
        values = "400 800 1600 2000 2400".split(" ")
        for value in values:
            acual_value = int(value) - 2
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()

                expected = f'The next leap year after {acual_value} is {acual_value+2}'
                self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{acual_value}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

if __name__ == '__main__':
    unittest.main()