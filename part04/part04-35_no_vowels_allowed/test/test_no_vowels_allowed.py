import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.no_vowels_allowed'
function = 'no_vowels'

def get_correct(test_case: str) -> str:
    return "".join([x for x in test_case if x not in "aeiou"])


@points('4.no_vowels_allowed')
class NoVowelsAllowedTest(unittest.TestCase):
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
            from src.no_vowels_allowed import no_vowels
        except:
            self.assertTrue(False, 'Your code should contain function named as no_vowels(my_string: str)')
        try:
            no_vowels = load(exercise, function, 'en')
            no_vowels("abc")
        except:
            self.assertTrue(False, 'Make sure, that function can be called as no_vowels("abc")')

    def test_2_type_of_return_value(self):
        no_vowels = load(exercise, function, 'en')
        val = no_vowels("abc")
        self.assertTrue(type(val) == str, 'Function no_vowels does not return value of string type when calling no_vowels("abc").')
    
    def test_3_one_word(self):
        for test_case in ["testword", "abracadabra", "ananas", "fizzbuzz", "aeoli", "abcdefghijklmnopqrstuvwxyz"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_vowels = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = no_vowels(test_case)

                self.assertEqual(correct, test_result, f'The returned string\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_vowels("{test_case}")')
if __name__ == '__main__':
    unittest.main()