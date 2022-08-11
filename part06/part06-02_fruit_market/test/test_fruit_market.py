import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.fruit_market'
function = 'read_fruits'

def get_correct() -> dict:
    pass

testdata = ["fruits.csv"]

import os
from shutil import copyfile

@points('6.fruit_market')
class FruitMarketTest(unittest.TestCase):
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
                from src.fruit_market import read_fruits
            except:
                self.fail( 'Your code must include function read_fruits()!')

    def test_2_return_type(self):
            read_fruits = load(exercise, function, 'en')
            try:
                val = read_fruits()
            except:
                 self.assertTrue(False, f"Ensure that function can be called:\nread_fruits()")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == dict, f"Function {function} should return a dictionary, now it returns value {val} which is of type {taip}.")

    def test_3_test_return_value(self):
            read_fruits = load(exercise, function, 'en')

            val = read_fruits()
            correct = {'banana': 6.5, 'apple': 2.85, 'pineapple': 9.5, 'mango': 6.75, 'orange': 5.5, 'fig': 11.0, 'tangerine': 5.75, 'pomegranate': 11.5}
            
            self.assertTrue(val == correct, f"Your function should return\n{correct}\nbut it returns\n{val}")
            
if __name__ == '__main__':
    unittest.main()
