import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap

exercise = 'src.neighbours_in_list'
function = 'longest_series_of_neighbours'

def get_correct(test_case: list) -> list:
    pass


@points('4.neighbours_in_list')
class NeigboursInListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_4_lists_2(self):
        test_cases = {(1,2,3,0,1,2,3,4,5,3,4,5,1,2,3): 6,
                      (0,1,2,3,4,5,9,10,11,2,3,4): 6,
                      (1,3,5,7,10,11,14,15,19,20,21,22,23,24,25): 7}
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


                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} with the test input {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {list(test_case2)} but it is {list(test_case)}.")

    def test_5_lists_3(self):
        test_cases = {(1,2,3,5,6,7,6,5,6,7,10,11,10): 7,
                      (0,1,2,1,5,8,7,9,2,3,2): 4,
                      (5,3,4,2,3,1,2,3,9,8,7,8,7,6,7,6): 8}
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


                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} with the test input {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {list(test_case2)} but it is {list(test_case)}.")
              
if __name__ == '__main__':
    unittest.main()