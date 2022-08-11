import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.incorrect_lottery_numbers'
function = "filter_incorrect"
datafile = "correct_numbers.csv"

def clear_files():
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

filename = "lottery_numbers.csv"

import os
from shutil import copyfile

@points('6.incorrect_lottery_numbers')
class IncorrectLotteryNumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not excpected")]):
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
         os.remove(filename)

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions should be included in the 
if __name__ == "__main__":
block. The following code should be moved:
"""
        self.assertTrue(ok, message+line)


    def test_1_function_exists(self):
        try:
            from src.incorrect_lottery_numbers import filter_incorrect
        except:
            self.fail('Your code should contain a function filter_incorrect()')
 
    def test_2_creates_file(self):
        filter_incorrect = load(exercise, function, 'en')
        try:
            filter_incorrect()
        except:
            self.assertTrue(False, 'Ensure that function filter_incorrect() can be called')
        self.assertTrue(file_exists(datafile), f"Program does not create file {datafile} at all.")

    def test_3_correct_content(self):
        filter_incorrect = load(exercise, function, 'en')
        filter_incorrect()

        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Reading file {datafile} content throws an error")

        corr = ["week 1;17,19,35,23,8,20,36","week 4;21,2,22,14,4,28,38","week 9;8,13,25,12,33,34,35",
                "week 10;29,27,30,13,7,38,26","week 11;34,3,7,24,16,20,38","week 20;32,28,25,19,4,2,3",
                "week 22;10,23,24,33,31,21,2","week 23;34,28,14,33,18,6,9","week 26;8,17,26,9,28,25,27",
                "week 34;11,4,33,17,37,1,8","week 36;16,4,12,32,19,34,28",
                "week 49;31,22,11,6,33,38,35","week 50;35,5,7,24,8,22,21"]
        for c in corr:
            self.assertTrue(c in content, f"File {datafile} should contain a line {c} but it is not found.")

    def test_4_incorrect_content(self):
        filter_incorrect = load(exercise, function, 'en')
        filter_incorrect()
        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Reading file {datafile} content throws an error")

        corr = ["week x;23,29,38,1,35,18,25","week 8;32,21,26,1,15aa,14,17","week 1a5;17,8,38,18,9,32,25",
                    "week 21;25,8,18,33,13,11","week xx24;37,8,25,30,23,24,19","week 27;11,1,Ccy,31,9,20,24",
                    "week rrrsas;29,20,19,5,26,11,36","week **.';32,25,36,28,21,15,9",
                    "week cca:mC;12,32,30,28,4,16,20","week 51;rxXX,17,20,27,11,30,5",
                    "week 52;29,26,11,21,20,29,5", "week 31;6,38,4,-26,32,24,34", "week 25;2,25,27,310,8,7,4"]
        for c in corr:
            self.assertFalse(c in content, f"File {datafile} should NOT contain an invalid line {c}.")


    def test_5_test_file_length(self):
        filter_incorrect = load(exercise, function, 'en')
        filter_incorrect()

        try:
            content = get_content()
        except: 
            self.assertTrue(False, f"Reading file {datafile} content throws an error")

        self.assertEqual(len(content), 37, f"File {datafile} should contain 37 lines, now there are {len(content)} lines.")


if __name__ == '__main__':
    unittest.main()
