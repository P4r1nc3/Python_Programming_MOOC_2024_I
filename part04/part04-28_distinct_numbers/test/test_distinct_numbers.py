import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.distinct_numbers'
function = 'distinct_numbers'

def get_correct(test_case: list) -> list:
    pass

@points('4.distinct_numbers')
class DistinctNumbersTest(unittest.TestCase):
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
            from src.distinct_numbers import distinct_numbers
        except:
            self.assertTrue(False, 'Your code should contain function named as distinct_numbers(my_list: list)')
        try:
            distinct_numbers = load(exercise, function, 'en')
            distinct_numbers([1,2])
        except:
            self.assertTrue(False, 'Test function call\ndistinct_numbers([1,2])')

    def test_2_type_of_return_value(self):
        distinct_numbers = load(exercise, function, 'en')
        val = distinct_numbers([1,2])
        self.assertTrue(type(val) == list, f"Function {function} does not return list with parameter value [1,2].")
    
    def test_3_numbers_1(self):
        test_cases = {(1,2,3,1,2,3): [1,2,3], 
                      (5,6,7,8,8,9,9,5): [5,6,7,8,9],
                      (1,10,1,100,1,1000): [1,10,100,1000]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                longest_ones = load(exercise, function, 'en')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = longest_ones(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected resul {correct} when calling distinct_numbers({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

    def test_4_numbers_2(self):
        test_cases = {(3,2,1,3,2,1,3,2,1): [1,2,3], 
                      (9,8,7,6,9,8,7,6,10,3,3,3,3,1): [1,3,6,7,8,9,10],
                      (-1,-2,-1,-2,-3,-3,-3,0,0): [-3,-2,-1,0]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                longest_ones = load(exercise, function, 'en')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = longest_ones(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected resul {correct} when calling distinct_numbers({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")
              
if __name__ == '__main__':
    unittest.main()