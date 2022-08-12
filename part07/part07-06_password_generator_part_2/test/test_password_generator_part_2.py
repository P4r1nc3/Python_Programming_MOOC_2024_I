import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from string import ascii_lowercase, digits

exercise = 'src.password_generator_part_2'
function = "generate_strong_password"
punctuation = "!?=+-()#"

def chars_ok(s: str, g: str):
    return len([x for x in s if x not in g]) == 0

def contains(s: str, g: str):
    return any([x in s for x in g])

@points('7.password_generator_part_2')
class PasswordGenerator2Test(unittest.TestCase):
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

    def function_exists(self):
        try:
            from src.password_generator_part_2 import generate_strong_password
        except:
            self.assertTrue(False, "Your code should contain function named as generate_strong_password(length: int, numbers: bool, special_characters: bool)")

    def test2_type_of_return_value(self):
        try:
            from src.password_generator_part_2 import generate_strong_password
            val = generate_strong_password(2,False,False)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == str, 
                f"The function generate_strong_password is expected to return a value whichs type is string. Now it returns a value {val} whichs type is {taip} when calling the function with the parameters (2, False, False)")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter values (2, False, False)")

    def test3_uses_import_expressions(self):
        with open("src/password_generator_part_2.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Your program does not import random-library with the import expression.")

    def test4_test_only_letters(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                generate_strong_password = load(exercise, function, 'en')

                val1 = generate_strong_password(test_case, False, False)
                val2 = generate_strong_password(test_case, False, False)

                self.assertTrue(len(val1) == test_case, f"Length of the password is {len(val1)}, but it should be {test_case} when the parameter is {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase), f"The password contains other characters than allowed: \n{val1} \nwhen the parameters are {test_case, False, False}")
                self.assertTrue(chars_ok(val2, ascii_lowercase), f"The password contains other characters than allowed: \n{val2} \nwhen the parameters are {test_case, False, False}") 
                self.assertNotEqual(val1, val2, f"Calling the function returns same password each time: \n{val1} \nwhen the parameter is {test_case}")

    def test5_test_letters_and_numbers(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                generate_strong_password = load(exercise, function, 'en')

                val1 = generate_strong_password(test_case, True, False)
                val2 = generate_strong_password(test_case, True, False)

                self.assertTrue(len(val1) == test_case, f"Length of the password is {len(val1)}, but it should be {test_case} when the parameter is {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + digits), f"The password contains other characters than allowed: \n{val1} \nwhen the parameters are {test_case, True, False}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + digits), f"The password contains other characters than allowed: \n{val2} \nwhen the parameters are {test_case, True, False}") 
                self.assertTrue(contains(val1, digits), f"The password does not contain a single character from the set '{digits}': {val1} when the parameters are {test_case, True, False} ")
                self.assertTrue(contains(val1, ascii_lowercase), f"The password does not contain a single character from the set '{ascii_lowercase}': {val1} when the parameters are {test_case, True, False} ") 
                self.assertNotEqual(val1, val2, f"Calling the function returns same password each time: {val1} when the parameters are {test_case, False, True}")

    def test6_test_letters_and_special_characters(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                generate_strong_password = load(exercise, function, 'en')

                val1 = generate_strong_password(test_case, False, True)
                val2 = generate_strong_password(test_case, False, True)

                self.assertTrue(len(val1) == test_case, f"Length of the password is {len(val1)}, but it should be {test_case} when the parameter is {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + punctuation), f"The password contains other characters than allowed: \n{val1} \nwhen the parameters are {test_case, False, True}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + punctuation), f"The password contains other characters than allowed: \n{val2} \nwhen the parameters are {test_case, False, True}") 
                self.assertTrue(contains(val1, ascii_lowercase), f"The password does not contain a single character from the set '{ascii_lowercase}': {val1} when the parameters are {test_case, False, True} ") 
                self.assertTrue(contains(val1, punctuation), f"The password does not contain a single character from the set '{punctuation}': {val1} when the parameters are {test_case, False, True} ")
                self.assertNotEqual(val1, val2, f"Calling the function returns same password each time: {val1} when the parameters are {test_case, False, True}")

    def test7_test_all(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                generate_strong_password = load(exercise, function, 'en')

                val1 = generate_strong_password(test_case, True, True)
                val2 = generate_strong_password(test_case, True, True)

                self.assertTrue(len(val1) == test_case, f"Length of the password is {len(val1)}, but it should be {test_case} when the parameter is {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + punctuation + digits), f"The password contains other characters than allowed: \n{val1} \nwhen the parameters are {test_case, True, True}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + punctuation + digits), f"The password contains other characters than allowed: \n{val2} \nwhen the parameters are {test_case, True, True}") 
                self.assertTrue(contains(val1, punctuation), f"The password does not contain a single character from the set '{punctuation}': {val1} when the parameters are {test_case, True, True} ")
                self.assertTrue(contains(val1, digits), f"The password does not contain a single character from the set '{digits}': {val1} when the parameters are {test_case, True, True} ") 
                self.assertTrue(contains(val1, ascii_lowercase), f"The password does not contain a single character from the set '{ascii_lowercase}': {val1} when the parameters are {test_case, True, True} ") 
                self.assertNotEqual(val1, val2, f"Calling the function returns same password each time: {val1} when the parameters are {test_case, True, True}")

if __name__ == '__main__':
    unittest.main()