import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.valid_pic'
function = "is_it_valid"

@points('7.valid_pic')
class PICTest(unittest.TestCase):
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
            from src.valid_pic import is_it_valid
        except:
            self.assertTrue(False, "Your program should contain function named as is_it_valid(pic: str)")

    def test2_type_of_return_value(self):
        try:
            from src.valid_pic import is_it_valid
            val = is_it_valid("230827-906F")
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == bool, f"The function is_it_valid is expected to return a value whichs type is bool. Now it returns a value {val} whichs type is {taip} when calling the function with the parameter '230827-906F'")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter values ('230827-906F')")

    def test3_uses_import_expression(self):
        with open("src/valid_pic.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "datetime" in cont , 
                f"Your program does not import datetime-library with the import expression.")

    def test4_test_valid_ones(self):
        test_cases = ["080842-720N","110986+713J","200614+561E","050882-437X",
                    "280360+081K","130767-6199","140216+523M","270561-080S",
                    "260168+0989","080283+440C","290531+1054","100400A644E",
                    "160340-670N","140375-767J","200872+5301","200642-4481",
                    "090790+214K","160759-346B","110874+273E","210420-183U",
                    "290103A605T","110705A4064","201106A660L","040705A810M",
                    "030103A493D","280905A4548","290200A1239"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                is_it_valid = load(exercise, function, 'en')

                try:
                    val = is_it_valid(test_case)
                except:
                    self.fail(f"Make sure, that function works with the parameter value '{test_case}'")


                self.assertTrue(val, f"Function returns '{val}' with the parameter value '{test_case}', even it is valid personal identification code.")

    def test5_test_invalid_dates(self):
        test_cases = ["081842-720N","310286+713J","290200-1239","290200+1239"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                is_it_valid = load(exercise, function, 'en')

                try:
                    val = is_it_valid(test_case)
                except:
                    self.fail(f"Make sure, that function works with the parameter value '{test_case}'")

                self.assertFalse(val, f"Function returns '{val}' with the parameter value '{test_case}' although date of the personal identification code is not a valid date.")

    def test5_test_bad_control_characters(self):
        test_cases = ["081142-720N","310186+713J","230200+1234"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                is_it_valid = load(exercise, function, 'en')

                try:
                    val = is_it_valid(test_case)
                except:
                    self.fail(f"Make sure, that function works with the parameter value '{test_case}'")

                self.assertFalse(val, f"Function returns '{val}' with the parameter value '{test_case}' although control character of the personal identification is not valid.")

    def test6_test_incorrect_length(self):
        test_cases = ["230827-906F1","030103A493DD"]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                is_it_valid = load(exercise, function, 'en')

                try:
                    val = is_it_valid(test_case)
                except:
                    self.fail(f"Make sure, that function works with the parameter value '{test_case}'")

                self.assertFalse(val, f"Function returns '{val}' with the parameter value '{test_case}' although length of the personal identification is incorrect.")

if __name__ == '__main__':
    unittest.main()