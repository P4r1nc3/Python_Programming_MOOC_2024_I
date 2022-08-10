import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.factorials'
function = 'factorials'

def get_correct(test_case: int) -> dict:
    k = lambda n: reduce(lambda a,b: a * b, range(1, n + 1))
    return {i: k(i) for i in range (1, test_case + 1)}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.factorials')
class FactorialsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message =  """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.factorials import factorials
        except:
            self.assertTrue(False, 'Your code should contain function named as factorials(n: int)')
        try:
            factorials = load(exercise, function, 'en')
            factorials(1)
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nfactorials(1)')

    def test_2_type_of_return_value(self):
        factorials = load(exercise, function, 'en')
        val = factorials(1)
        self.assertTrue(type(val) == dict, f"Function {function} should return value which type is dict.")
    
    def test_3_factorials(self):
        test_cases = (1,2,4,3,5,6,8,10)
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                factorials = load(exercise, function, 'en')

                value = factorials(test_case)
                correct = get_correct(test_case)

                self.assertEqual(len(correct), len(value), f"The returned dictionary should contain {len(correct)} items, but it contains {len(value)} items: \n{value}\nwhen calling factorials({test_case})") 
                self.assertEqual(value, correct, f"The result \n{value}\ndoes not match with the model solution \n{correct}\nwhen calling factorials({test_case})") 
              
if __name__ == '__main__':
    unittest.main()