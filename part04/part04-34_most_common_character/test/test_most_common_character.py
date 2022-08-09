import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.most_common_character'
function = 'most_common_character'

def get_correct(test_case: str) -> str:
    return max([(test_case.count(x), x) for x in test_case])[1]

def f(mj):
    return f'"{mj}"'

@points('4.most_common_character')
class MostCommonCharacterTest(unittest.TestCase):
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
            from src.most_common_character import most_common_character
        except:
            self.assertTrue(False, 'Your code should contain function named as most_common_character(my_string: str)' )
        try:
            from src.most_common_character import most_common_character
            most_common_character("abc")
        except:
            self.assertTrue(False, 'Make sure, that function can be called as most_common_character("abc")' )

    def test_2_type_of_return_value(self):
        most_common_character = load(exercise, function, 'en')
        val = most_common_character("abc")
        self.assertTrue(type(val) == str, 'Function most_common_character does not return value of string type when calling most_common_character("abc")')
    
    def test_3_one_word(self):
        for test_case in ["aaabb", "aabbbbc", "abcabca","xyzxyzyyxyz", "composer"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                most_common_character = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = most_common_character(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling most_common_character({f(test_case)})")

    def test_4_several_words(self):
        for test_case in ["aaaa bbb ccc ddddd bbb", "she sells seasell", "xyz xyz xyz zzzzorro"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                most_common_character = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = most_common_character(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling most_common_character({f(test_case)})")
 
if __name__ == '__main__':
    unittest.main()