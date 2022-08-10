import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.times_ten'
function = 'times_ten'

def get_correct(a: int, b: int) -> dict:
    return {x: x * 10 for x in range(a, b + 1)}

@points('5.times_ten')
class Times10Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message =  """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.times_ten import times_ten
        except:
            self.assertTrue(False, 'Your code should contain function named as times_ten(start_index: int, end_index: int)')
        try:
            times_ten = load(exercise, function, 'en')
            times_ten(1,2)
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\ntimes_ten(1, 2)')

    def test_2_type_of_return_value(self):
        times_ten = load(exercise, function, 'en')
        val = times_ten(1,2)
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Function {function} should return value which is dict-type, now it returns value {val} which is {taip}-type.")
    
    def test_3_numbers(self):
        test_cases = ((1,3),(0,6),(2,8),(20,23),(100,110))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_tart = get_stdout()
                times_ten = load(exercise, function, 'en')

                value = times_ten(test_case[0], test_case[1])
                correct = get_correct(test_case[0], test_case[1])

                self.assertEqual(len(correct), len(value), f"The returned dictionary should contain {len(correct)} items, but it contains {len(value)} items: \n{value} when the parameters are {test_case}")
                self.assertEqual(value, correct, f"The result \n{value}\ndoes not match with the model solution \n{correct}\nwhen the parameters are\n{test_case}")
              
if __name__ == '__main__':
    unittest.main()
