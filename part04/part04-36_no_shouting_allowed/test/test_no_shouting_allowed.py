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
class NoShoutingAllowed(unittest.TestCase):
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
            from src.no_shouting_allowed import no_shouting
        except:
            self.assertTrue(False, 'Your code should contain function named as no_shouting(my_list: list)')
        try:
            from src.no_shouting_allowed import no_shouting
            no_shouting(["Abc"])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows no_shouting(["Abc"])')

    def test_2_no_return_value(self):
        no_shouting = load(exercise, function, 'en')
        val = no_shouting(["Abc"])
        self.assertTrue(type(val) == list, f'Function {function} does not return list when calling \nno_shouting(["Abc"])')
    
    def test_3_uppercase_ones_not_consecutively(self):
        for test_case in [["FIRST", "second", "THIRD", "fourth"], ["aaaa", "BBBB", "cccc", "dddd", "EEEE", "ffff", "GGGG"]]:
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