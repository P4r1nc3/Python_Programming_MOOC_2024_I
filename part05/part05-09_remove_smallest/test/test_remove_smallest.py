import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.remove_smallest'
function = 'remove_smallest'


@points('5.remove_smallest')
class RemoveSmallestTest(unittest.TestCase):
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
            from src.remove_smallest import remove_smallest
        except:
            self.assertTrue(False, 'Your code should contain function named as remove_smallest(luvut: list)' )
        try:
            from src.remove_smallest import remove_smallest
            remove_smallest([1, 2])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nremove_smallest([1,2])' )

    def test_2_type_of_return_value(self):
        remove_smallest = load(exercise, function, 'en')
        val = remove_smallest([1])
        self.assertTrue(val == None, f"Function {function} should not return a value, now type of return value is {type(val)}.")
    
    def test_3_lists(self):
        test_cases = ([1,2,3,5,6], [9,7,5,3], [10,13,15,9,11,12,14], [100,10], [1,2,3,-1,-2,-3], [-4,-5,-6,-3,-2])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                out_at_start = get_stdout()
                remove_smallest = load(exercise, function, 'en')
                
                correct = [x for x in test_case if x != min(test_case)]
                test_case2 = test_case[:]

                try:
                    remove_smallest(test_case)
                except:
                    self.assertTrue(False, f"Make sure, that the function works when the input is\n{test_case2}")

                self.assertEqual(correct, test_case, f"The result\n{test_case}\ndoes not match with the model solution\n{correct}\nwhen the input is\n{test_case2}")

if __name__ == '__main__':
    unittest.main()