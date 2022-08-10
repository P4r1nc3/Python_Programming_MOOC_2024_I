import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.longest_string'
function = 'longest'

@points('5.longest_string')
class LongestStringTest(unittest.TestCase):
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
            from src.longest_string import longest
        except:
            self.assertTrue(False, 'Your code should contain function named as longest(strings: list)' )
        try:
            from src.longest_string import longest
            longest(["ab","a"])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nlongest(["ab","a"])' )

    def test_2_type_of_return_value(self):
        longest = load(exercise, function, 'en')
        val = longest(["ab","a"])
        self.assertTrue(type(val) == str, f'Function {function} does not return value of string type when calling longest(["ab","a"])')
    
    def test_3_lists(self):
        test_cases = ("first second third", "ab abcd abc acbdefg a abcd aa", "orange apple milkshake banana pear", "sheila sells seashells on the seashore")
        for tc in test_cases:
            test_case = tc.split()
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                longest = load(exercise, function, 'en')
                
                correct = max(test_case, key=lambda x : len(x))
                
                try:
                    test_result = longest(test_case)
                except:
                    self.assertTrue(False, f"Make sure, that the function works when the list is\n{test_case}")

                self.assertEqual(correct, test_result, f"The result '{test_result}' does not match with the model solution '{correct}' when the list is {test_case}")
                
              
if __name__ == '__main__':
    unittest.main()