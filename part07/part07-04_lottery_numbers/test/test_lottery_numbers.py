import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.lottery_numbers'
function = "lottery_numbers"

def within_limits(lst: list, low: int, high: int):
    return len([x for x in lst if x < low or x > high]) == 0

def unique(lst: list):
    return len(set(lst)) == len(lst)

def is_sorted(lst: list):
    return sorted(lst) == lst

@points('7.lottery_numbers')
class LotteryNumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
            from src.lottery_numbers import lottery_numbers
        except:
            self.assertTrue(False, "Your code should contain function named as lottery_numbers(amount: int, lower: int, upper: int)")

    def test2_type_of_return_value(self):
        try:
            from src.lottery_numbers import lottery_numbers
            val = lottery_numbers(1, 1, 10)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, 
                f"The function lottery_numbers is expected to return a value whichs type is list. Now it returns a value {val} whichs type is {taip} when calling the function with the parameters (1,1,10)")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter values (1,1,10)")

    def test3_uses_import_expression(self):
        with open("src/lottery_numbers.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Your program does not import random-library with the import expression.")
    

    def test4_test_with_values(self):
        test_cases = [(3,2,22), (5,10,100), (7,1,39)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                lottery_numbers = load(exercise, function, 'en')

                val1 = lottery_numbers(test_case[0], test_case[1], test_case[2])
                val2 = lottery_numbers(test_case[0], test_case[1], test_case[2])

                self.assertTrue(len(val1) == test_case[0], f"The list contains {len(val1)} items. It should contain {test_case[0]} items, when the parameters are {test_case}: {val1}")
                self.assertTrue(unique(val1), f"Values in the list are not unique: \n{val1} \newhen the parameters were {test_case}")
                self.assertTrue(unique(val2), f"Values in the list are not unique: \n{val2} \nwhen the parameters were {test_case}")
                self.assertNotEqual(val1, val2, f"Calling the function returns same values each time: \n{val1} \nwhen the paramaters are {test_case}")
                self.assertTrue(is_sorted(val1), f"Values in the list are not in ascending order: \n{val1} \nwhen the paramaters are {test_case}")
                self.assertTrue(within_limits(val1, test_case[1], test_case[2]), 
                    f"The list have too small or too big item when the parameters were {test_case}: \n{val1} ")
                self.assertTrue(within_limits(val2, test_case[1], test_case[2]), 
                    f"The list have too small or too big item when the parameters were {test_case}: \n{val2} ")

if __name__ == '__main__':
    unittest.main()
