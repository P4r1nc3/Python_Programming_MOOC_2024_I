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
class VokaalitPoisTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_4_sentences(self):
        for test_case in ["this is a longer sentence", "a test with more than one word", "hi everybody!"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_vowels = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = no_vowels(test_case)

                self.assertEqual(correct, test_result, f'The returned string\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_vowels("{test_case}")')

    def test_5_no_vowels(self):
        for test_case in ["xzcvb", "grrrrr", "bdfghjklvwy"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_vowels = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = no_vowels(test_case)

                self.assertEqual(correct, test_result, f'The returned string\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_vowels("{test_case}")')

    def test_6_only_vowels(self):
        for test_case in ["aeio","uuuuoooaaaa"]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_vowels = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_result = no_vowels(test_case)

                self.assertEqual(correct, test_result, f'The returned string\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_vowels("{test_case}")')

if __name__ == '__main__':
    unittest.main()