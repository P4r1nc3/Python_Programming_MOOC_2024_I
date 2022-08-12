import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.calculation_with_fractions'
function = "fractionate"

def format(l: list):
    return [str(x) for x in l]



@points('7.fractions')
class FractionsTest(unittest.TestCase):
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
            from src.calculation_with_fractions import fractionate
        except:
            self.assertTrue(False, "Your code should contain function named as fractionate(amount: int)")

    def test2_type_of_return_value(self):
        try:
            from src.calculation_with_fractions import fractionate
            val = fractionate(2)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"The function fractionate is expected to return a value whichs type is list. Now it returns a value {val} whichs type is {taip} When calling the function with the parameter 2")
        except:
            self.assertTrue(False, f"There was an error when the function was called with the parameter value 2")

    def test3_uses_import_expression(self):
        with open("src/calculation_with_fractions.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "fractions" in cont, 
                f"Your program does not import fractions-library with the import expression.")

    def test4_test_with_values(self):
        f = Fraction
        test_cases = [2, 3, 4, 7, 11, 13, 8]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                fractionate = load(exercise, function, 'en')

                val = fractionate(test_case)
                correct = [f(1, test_case)] * test_case

                for i in range(3):
                    self.assertEqual(val, correct, 
                        f"The result of the function \n'{val}' \nwith the parameter value \n'{test_case}' \ndoes not match with the model solution \n'{correct}'.")

if __name__ == '__main__':
    unittest.main()