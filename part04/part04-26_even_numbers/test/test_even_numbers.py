import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.even_numbers'
function = 'even_numbers'

def get_correct(test_case: list) -> list:
    pass


@points('4.even_numbers')
class EvenNumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.even_numbers import even_numbers
        except:
            self.assertTrue(False, 'Your code should contain function named as even_numbers(my_list: list)')
        try:
            from src.even_numbers import even_numbers
            even_numbers([1,2])
        except:
            self.assertTrue(False, 'Does following function call work?\neven_numbers([1,2])')

    def test_2_type_of_return_value(self):
        even_numbers = load(exercise, function, 'en')
        val = even_numbers([1,2])
        self.assertTrue(type(val) == list, f"Function {function} does not return list with parameter values [1,2].")
    
    def test_3_numbers_1(self):
        test_cases = {(1,2,3,4,5,6): [2,4,6], 
                      (1,2,3,4,8,9,10,12,14,15): [2,4,8,10,12,14],
                      (1,3,5,7,9,2,4,6,8,10): [2,4,6,8,10]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                pisimmat = load(exercise, function, 'en')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(sorted(correct), sorted(test_result), f"The result {test_result} does not match with the expected answer {correct} when calling even_numbers({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

    def test_4_numbers_2(self):
        test_cases = {(99,100,101,100,99,100,101): [100,100,100], 
                      (6,6,6,6,5,6,6,6,6,6,5): [6,6,6,6,6,6,6,6,6],
                      (1,1,2,2,1,1,2,2): [2,2,2,2]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                longest_ones = load(exercise, function, 'en')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = longest_ones(list(test_case))

                self.assertEqual(sorted(correct), sorted(test_result), f"The result {test_result} does not match with the expected answer {correct} when calling even_numbers({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()