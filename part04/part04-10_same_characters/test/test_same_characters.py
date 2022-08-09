import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.same_characters'

@points('4.same_characters')
class SameCharactersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_2_function_exists(self):
        try:
            from src.same_characters import same_chars
        except:
            self.assertTrue(False, f'Your code should contain function named as same_chars')

    def test_3_function_can_be_called1(self):
        try:
            from src.same_characters import same_chars
            same_chars("coder", 1, 10)
        except:
            self.assertTrue(False, f'Make sure, that function same_chars can be called as follows:\nsame_chars("coder", 1, 10)')
        try:
            from src.same_characters import same_chars
            same_chars("coder", 10, 1)
        except:
            self.assertTrue(False, f'Make sure, that function same_chars can be called as follows:\nsame_chars("coder", 10, 1)')

if __name__ == '__main__':
    unittest.main()