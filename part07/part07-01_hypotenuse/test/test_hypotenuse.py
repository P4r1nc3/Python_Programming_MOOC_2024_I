import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.hypotenuse'
function = "hypotenuse"

@points('7.Hypotenuse')
class hypotenuseTest(unittest.TestCase):
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
            from src.hypotenuse import hypotenuse
        except:
            self.assertTrue(False, "Your code should contain function named as hypotenuse(leg1: float, leg2: float)")

    def test2_type_of_return_value(self):
        try:
            from src.hypotenuse import hypotenuse
            val = hypotenuse(1.0,1.0)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == float, f"Function hypotenuse should return a value whichs type is float, now it returns a value {val} whichs type is {taip}")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter values (1.0, 1.0)")

    def test3_uses_import_expression(self):
        with open("src/hypotenuse.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "math" in cont, f"Your program does not import sqrt-function from the math module with import expression.")
    

    def test4_test_with_values(self):
        test_cases = {(3.0, 4.0): 5.0, (5.0, 12.0): 13.0}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                hypotenuse = load(exercise, function, 'en')

                val = hypotenuse(test_case[0], test_case[1])

                self.assertEqual(val, test_cases[test_case], f"The function returned value {val} with parameter values {test_case}, the correct return value would have been {test_cases[test_case]}")
              
if __name__ == '__main__':
    unittest.main()