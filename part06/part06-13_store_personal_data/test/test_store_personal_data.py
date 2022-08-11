import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.store_personal_data'
function = "store_personal_data"
datafile = 'people.csv'

def clear_file():
    with open(datafile, "w"):
        pass

def get_content():
    with open(datafile) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0] 

def format(f):
    return "\n".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

@points('6.store_personal_data')
class StorePersonalDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions should be included in the 
if __name__ == "__main__":
block. The following code should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.store_personal_data import store_personal_data
        except:
            self.fail("Your program should contain a function store_personal_data(person: tuple)")
        try:
            store_personal_data(('Timothy Test', 45, 160.0))
        except Exception as e:
            self.fail("The following function call throws an error store_personal_data(('Timothy Test', 45, 160.0)):\n" + e)


    def test_2_write_one_person_1(self):
        test_case = ('Timothy Test', 45, 160.0)
        clear_file()
        correct = ["Timothy Test;45;160.0"]
        store_personal_data = load(exercise, function, 'en')
        try:
            store_personal_data(test_case)
        except OSError as ioe:
            self.fail(f"Function throws an error with parameters {test_case}: {ioe}")
        self.assertTrue(file_exists(datafile), f"File {datafile} cannot be found after the function is executed!")

        data = get_content()

        self.assertTrue(len(data) == 1, 
            f"File {datafile} should contain 1 line after the function was called with empty file with parameters {test_case} - now there are {len(data)} lines.")

        self.assertEqual(data, correct, f"The contents of the file should be \n{format(correct)} \nbut they are \n{format(data)} \nwhen called with parameters {test_case}")
                      
if __name__ == '__main__':
    unittest.main()
