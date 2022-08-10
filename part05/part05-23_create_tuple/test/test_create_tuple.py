import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.create_tuple'
function = 'create_tuple'

@points('5.create_tuple')
class CreateTupleTest(unittest.TestCase):
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
            from src.create_tuple import create_tuple
        except:
            self.assertTrue(False, 'Your code should contain function named as create_tuple(x: int, y: int, z: int)' )
        try:
            from src.create_tuple import create_tuple
            create_tuple(1,2,3)
        except:
            self.assertTrue(False, 'Make sure,  hat following function call works:\ncreate_tuple(1,2,3)' )

    def test_2_type_of_return_value(self):
        create_tuple = load(exercise, function, 'en')
        val = create_tuple(1,2,3)
        self.assertTrue(type(val) == tuple, f'Function {function} does not return a tuple when calling create_tuple(1,2,3)')
    
    def test_3_tuples(self):
        test_cases = ((1,4,2), (10, 8, 5), (100, 101, 102), (-10, -11, -12), (55, 550, 5500))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                create_tuple = load(exercise, function, 'en')
                
                correct = (min(test_case), max(test_case), sum(test_case))
                
                try:
                    test_result = create_tuple(test_case[0], test_case[1], test_case[2])
                except:
                    self.assertTrue(False, f"Make sure that the function works when the parameters are {test_case}")

                self.assertEqual(correct, test_result, f"The result '{test_result}' does not match with the model solution '{correct}' when the parameters are {test_case}")
                
              
if __name__ == '__main__':
    unittest.main()