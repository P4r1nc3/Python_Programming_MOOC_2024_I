import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.largest_number'
function = 'largest'

def get_correct() -> dict:
    pass

testdata = ["numbers.txt"]

import os
from shutil import copyfile

@points('6.largest_number')
class LargestNumberTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not required")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be included inside
if __name__ == "__main__":
block. The following code needs to be relocated::
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
            try:
                from src.largest_number import largest
            except:
                self.assertTrue(False, f"Your code must include function largest()")

    def test_2_return_type(self):
            largest = load(exercise, function, 'en')

            try:
                val = largest()
            except:
                 self.assertTrue(False, f"Ensure that function can be called with\nlargest()")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == int, f"Function {function} should return an integer, now it returns value {val} which is of type {taip}.")
    
    def test_3_test_return_value(self):
            largest = load(exercise, function, 'en')

            val = largest()
            correct = 9988
            
            self.assertEqual(val, correct, f"Function returns {val}, correct answer is {correct}.")
          
if __name__ == '__main__':
    unittest.main()
