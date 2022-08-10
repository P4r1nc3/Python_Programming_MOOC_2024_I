import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.items_multiplied_by_two'
function = 'double_items'


@points('5.double_items')
class DoubleItemsTest(unittest.TestCase):
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
            from src.items_multiplied_by_two import double_items
        except:
            self.assertTrue(False, 'Your code should contain function named as double_items(numbers: list)' )
        try:
            from src.items_multiplied_by_two import double_items
            double_items([1])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\ndouble_items([1])' )

    def test_2_type_of_return_value(self):
        double_items = load(exercise, function, 'en')
        val = double_items([1])
        self.assertTrue(type(val) == list, f"Function {function} does not return value of list type when calling double_items([1]).")
    
    def test_3_lists(self):
        test_cases = ([1,3,5,7], [2,6,4,8,2,6,4], [9,7,5,3,1], [10,100,1000,100,10], [9,9,9,9,9])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                double_items = load(exercise, function, 'en')
                
                correct = [x*2 for x in test_case]
                test_case2 = test_case[:]

                try:
                    test_result = double_items(test_case)
                except:
                    self.assertTrue(False, f"Make sure, that the function works when the input is\n{test_case2}")

                self.assertEqual(correct, test_result, f"The result\n{test_result} \ndoes not match with the model solution\n{correct} \nwhen the input is\n{test_case2}")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {test_case2} but it is {test_case}.")
              
if __name__ == '__main__':
    unittest.main()