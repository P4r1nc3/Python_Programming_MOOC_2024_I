import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.everything_reversed'
function = 'everything_reversed'

def get_correct(test_case: list) -> list:
    return [x[::-1] for x in test_case][::-1]
@points('4.everything_reversed')
class EverythingReversedTest(unittest.TestCase):
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
            from src.everything_reversed import everything_reversed
        except:
            self.assertTrue(False, 'Your code should contain function named as everything_reversed(my_list: list)')
        try:
            everything_reversed = load(exercise, function, 'en')
            everything_reversed(["abc"])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows everything_reversed(["abc"])')

    def test_2_type_of_return_value(self):
        everything_reversed = load(exercise, function, 'en')
        val = everything_reversed(["abc"])
        self.assertTrue(type(val) == list, "Function everything_reversed does not return list when calling everything_reversed(['abc'])")
    
    def test_3_short_ones(self):
        for test_case in [["abc","def"], ["first","second","third"], ["one","two","three"]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                everything_reversed = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = everything_reversed(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling formatted everything_reversed({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {test_case2} but it is {test_case}.")

    def test_4_longer_ones(self):
        for test_case in [["here", "is", "a", "little", "longer", "list", "with", "more", "words"],
                            ["abcd", "efghijklmnopqrstu", "vwxyz"]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                everything_reversed = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = everything_reversed(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling formatted everything_reversed({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {test_case2} but it is {test_case}.")
                
if __name__ == '__main__':
    unittest.main()