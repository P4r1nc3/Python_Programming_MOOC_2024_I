import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from string import ascii_lowercase

exercise = 'src.password_generator_part_1'
function = "generate_password"

def caseok(s: str):
    return len([x for x in s if x not in ascii_lowercase]) == 0



@points('7.password_generator_part_1')
class PasswordGenerator1Test(unittest.TestCase):
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
            from src.password_generator_part_1 import generate_password
        except:
            self.assertTrue(False, "Your code should contain function named as generate_password(length: int)")

    def test2_type_of_return_value(self):
        try:
            from src.password_generator_part_1 import generate_password
            val = generate_password(2)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == str,
                f"The function generate_password is expected to return a value whichs type is string. Now it returns a value {val} whichs type is {taip} when calling the function with the parameter (2)")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter value (2)")

    def test3_uses_import_expression(self):
        with open("src/password_generator_part_1.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont,
                f"Your program does not import random-library with the import expression.")

    def test4_test_with_values(self):
        test_cases = [2, 4, 5, 8, 11, 13, 20]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                generate_password = load(exercise, function, 'en')

                val1 = generate_password(test_case)
                val2 = generate_password(test_case)

                self.assertTrue(len(val1) == test_case, f"Length of the password is {len(val1)}, but it should be {test_case} when the parameter is {test_case}: {val1}")
                self.assertTrue(caseok(val1), f"The password contains other characters than lowercase letters: \n{val1} \nwhen the parameter was {test_case}")
                self.assertTrue(caseok(val2), f"The password contains other characters than lowercase letters: \n{val2} \nwhen the parameter was {test_case}") 
                self.assertNotEqual(val1, val2, f"Calling the function returns same password each time: \n{val1} \nwhen the parameter is {test_case}")

if __name__ == '__main__':
    unittest.main()