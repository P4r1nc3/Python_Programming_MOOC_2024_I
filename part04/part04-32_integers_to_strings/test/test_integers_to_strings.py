import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.integers_to_strings'
function = 'formatted'

def get_correct(test_case: list) -> list:
    return [f"{x:.2f}" for x in test_case]


@points('4.integers_to_strings')
class IntegersToStringsTest(unittest.TestCase):
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
            from src.integers_to_strings import formatted
            formatted([0.23])
        except:
            self.assertTrue(False, 'Your code should contain function named as formatted(my_list: list)')
        try:
            formatted = load(exercise, function, 'en')
            formatted([0.23])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows formatted([0.23])')


    def test_2_type_of_return_value(self):
        formatted = load(exercise, function, 'en')
        val = formatted([1.23])
        self.assertTrue(type(val) == list, "Function formatted does not return list with parameter value [1.23].")
       
if __name__ == '__main__':
    unittest.main()