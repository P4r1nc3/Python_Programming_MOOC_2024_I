import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.invert_dictionary'
function = 'invert'

def get_correct(test_case: dict) -> dict:
    return {test_case[x] : x  for x in test_case}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.invert_dictionary')
class InvertDictionaryTest(unittest.TestCase):
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
             from src.invert_dictionary import invert
        except:
            self.assertTrue(False, 'Your code should contain function named as invert(dictionary: dict)')
        try:
            invert = load(exercise, function, 'en')
            invert({1:10,2:20})
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\ninvert({1: 10, 2: 20})')


    def test_2_type_of_return_value(self):
        invert = load(exercise, function, 'en')
        test_case = {1:100} 
        try:
           val = invert({1:10})
        except:
            self.assertTrue(False, f'Make sure, that following function call works: invert({test_case})')
   
        self.assertTrue(val == None, f"Function {function} should not return anything, now it returns value which is {type(val)} type.")
    
    def test_3_invert(self):
        test_cases = ({1:10,2:20,3:30}, {-1:1, -2:2, -3:3, -5:5, -10:10}, {x : x * 100 for x in range(1,10)}, {x: x-1 for x in range(10,90,10)})
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                invert = load(exercise, function, 'en')
                
                test_case2 = test_case.copy()
                correct = get_correct(test_case)
                try:
                    invert(test_case)
                except:
                    self.assertTrue(False, f'Make sure, that following function call works: invert({test_case})')
   
                self.assertEqual(len(correct), len(test_case), f"The returned dictionary should contain {len(correct)} items, but it contains {len(test_case)} items: \n{test_case}\nwhen calling invert({test_case2})")
                self.assertEqual(test_case, correct, f"The result \n{test_case}\ndoes not match with the model solution \n{correct}\nwhen calling invert({test_case2})")
             
if __name__ == '__main__':
    unittest.main()