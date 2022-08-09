import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.sum_of_positives'
function = 'sum_of_positives'

def get_correct(test_case: list) -> list:
    return sum([x for x in test_case if x > 0])

@points('4.sum_of_positives')
class SumOfPositivesTest(unittest.TestCase):
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
            from src.sum_of_positives import sum_of_positives
        except:
            self.assertTrue(False, 'Your code should contain function named as sum_of_positives(my_list: list)')
        try:
            from src.sum_of_positives import sum_of_positives
            sum_of_positives([1,2])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nsum_of_positives([1,2])')

    def test_2_type_of_return_value(self):
        from src.sum_of_positives import sum_of_positives
        val = sum_of_positives([1,2])
        self.assertTrue(type(val) == int, f"Calling {function} does not return value of integer type with parameter values sum_of_positives([1,2])")
    
    def test_3_numbers_1(self):
        test_cases = ([1,-1,2,-2,3,-3], [-9,-7,-5,-2,0,1,3,5,7,5], list(range(-10,10)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                sum_of_positives = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = sum_of_positives(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the correct answer {correct} when calling sum_of_positives({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

    def test_4_numbers_2(self):
        test_cases = ([-10,-8,-6,-4,-2], [-100000,1,2,3,4,5], list(range(-1000,1000,100)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                sum_of_positives = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = sum_of_positives(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the correct answer {correct} when calling sum_of_positives({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()