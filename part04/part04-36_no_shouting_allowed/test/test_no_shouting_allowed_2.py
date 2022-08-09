import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
import os
import textwrap

exercise = 'src.no_shouting_allowed'
function = 'no_shouting'

def get_correct(test_case: list) -> list:
    return [x for x in test_case if not x.isupper()]

@points('4.no_shouting_allowed')
class NoShoutingAllowedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_4_uppercase_ones_consecutively(self):
        for test_case in [["FIRST", "SECOND", "third", "fourth", "fifth"], ["aaaa", "BBBB", "CCCC", "DDDD", "EEEE", "ffff", "GGGG", "HHHH"]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_shouting = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case_original = test_case[:]
                test_result = no_shouting(test_case)

                self.assertTrue(correct == test_result, f"The returned list\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_shouting({test_case_original})")

    def test_5_not_a_single_all_uppercase_word(self):
        for test_case in [["first", "Second", "third", "fourth", "fifth"], ["aaaa", "Bbbb", "CCCc", "ddDd", "Eeee", "ffff", "GggG", "hhhh"]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                no_shouting = load(exercise, function, 'en')

                correct = get_correct(test_case)
                test_case_original = test_case[:]
                test_result = no_shouting(test_case)

                self.assertTrue(correct == test_result, f"The returned list\n{test_result}\ndoes not match with the expected\n{correct}\nwhen calling no_shouting({test_case_original})")

if __name__ == '__main__':
    unittest.main()