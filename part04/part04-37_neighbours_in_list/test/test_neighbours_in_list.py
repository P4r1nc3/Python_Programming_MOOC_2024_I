import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.neighbours_in_list'
function = 'longest_series_of_neighbours'

def get_correct(test_case: list) -> list:
    pass


@points('4.neighbours_in_list')
class NeighboursInListTest(unittest.TestCase):
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
            from src.neighbours_in_list import longest_series_of_neighbours
        except:
            self.assertTrue(False, 'Your code should contain function named as longest_series_of_neighbours(my_list: list)')
        try:
            longest_series_of_neighbours([1,2])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows longest_series_of_neighbours([1, 2])')

    def test_2_type_of_return_value(self):
        longest_series_of_neighbours = load(exercise, function, 'en')
        val = longest_series_of_neighbours([1,2])
        self.assertTrue(type(val) == int, f"Function {function} does not return value of integer type with parameter value [1,2].")
    
    def test_3_lists_1(self):
        test_cases = {(1,2,3,5,6,9,10): 3,
                      (0,2,4,5,6,7,10,11,12,100,101): 4,
                      (1,3,5,7,10,11,14,15,19,20,21,22,23,24,25,30): 7}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                longest_series_of_neighbours = load(exercise, function, 'en')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                try:
                    test_result = longest_series_of_neighbours(list(test_case))
                except:
                    self.assertTrue(False, f"Make sure that method works with parameter value {test_case2}.")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when calling function with the parameter value {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {list(test_case2)} but it is {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()