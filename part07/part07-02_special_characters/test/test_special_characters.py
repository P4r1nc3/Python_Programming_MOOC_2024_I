import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.special_characters'
function = "separate_characters"



@points('7.special_characters')
class SpecialCharactersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
            from src.special_characters import separate_characters
        except:
            self.assertTrue(False, "Your code should contain function named as separate_characters(my_string: str)")

    def test2_type_of_return_value(self):
        from src.special_characters import separate_characters
        val = separate_characters("1.ö")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == tuple, f"The function separate_characters is expected to return a value, whichs type is tuple. Now it returns a value {val} whichs type is {taip} when calling the function with the parameter '1.ö'")
        self.assertTrue(len(val) == 3, f"The function separate_characters is expected to return tuple, which consist of three strings. Now it it returns a value {val} when calling the function with the parameter '1.ö'")

    def test3_uses_import_expression(self):
        with open("src/special_characters.py") as f:
            cont = f.read()
            self.assertTrue("ascii_letters" in cont,
                f"Your program does not use string constant ascii_letters of the the string module.")
            self.assertTrue("punctuation" in cont,
                f"Your program does not use string constant punctuation of the the string module.")

    def test4_test_with_values(self):
        test_cases = {"abc.!åäö": ("abc", ".!", "åäö"), 
                      "a. s, d: f; g* ": ("asdfg", ".,:;*", "     "), 
                      "Th¡s ¡s @ tést!!!! Or is it? Yes, it is.": ("ThsststOrisitYesitis", "@!!!!?,.", "¡ ¡  é      ")}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                seperate_characters = load(exercise, function, 'en')

                val = seperate_characters(test_case)

                for i in range(3):
                    self.assertEqual(val[i], test_cases[test_case][i], f"The string returned by the function \n'{val[i]}' \nwith the parameter value \n'{test_case}' \ndoes not match with the model solution \n'{test_cases[test_case][i]}'. The whole return value of the function was {val}.")
              
if __name__ == '__main__':
    unittest.main()
