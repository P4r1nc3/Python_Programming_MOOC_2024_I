import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.filtering_file_contents'
function = "filter_solutions"
datafile1 = 'correct.csv'
datafile2 = 'incorrect.csv'

import os
from shutil import copyfile

def get_correct() -> dict:
    pass

def clear_files():
    with open(datafile1, "w"), open(datafile2, "w"):
        pass

def get_content():
    with open(datafile1) as f, open(datafile2) as f2:
        return ([x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0],
               [x.replace("\n","") for x in f2.readlines() if len(x.strip()) > 0]) 

def format(f):
    return "\n".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def read(fname: str):
    with open(fname) as f:
        return [x.strip() for x in f.readlines() if len(x.strip()) > 0]

@points('6.filtering_file_contents')
class FilteringFileContentsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("No input is required")]):
            filename = "solutions.csv"
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        os.remove("solutions.csv")

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions should be included in the 
if __name__ == "__main__":
block. The following code should be moved:
"""
        self.assertTrue(ok, message+line)
    
    def test_1_function_exists(self):
        try:
            from src.filtering_file_contents import filter_solutions
        except:
            self.assertTrue(False, "The program should include a function filter_solutions()")

    def test_2_creates_file_1(self):
        filter_solutions = load(exercise, function, 'en')
        filter_solutions()
        self.assertTrue(file_exists('correct.csv'), "Program does not create file correct.csv at all.")

    def test_3_creates_file_2(self):
        filter_solutions = load(exercise, function, 'en')
        filter_solutions()
        self.assertTrue(file_exists('incorrect.csv'), "Program does not create file incorrect.csv at all.")


    def test_4_test_correct_length(self):
        filter_solutions = load(exercise, function, 'en')
        filter_solutions()

        try:
            content = read("correct.csv")
        except Exception as ioe: 
            self.fail("Reading file correct.csv throws an error: \n" + ioe)

        self.assertEqual(len(content), 42, f"The file correct.csv shoudl have 42 lines after the program is executed, now it has {len(content)} lines.")

    def test_5_test_incorrect_length(self):
        filter_solutions = load(exercise, function, 'en')
        filter_solutions()

        try:
            content = read("incorrect.csv")
        except Exception as ioe: 
            self.fail("Reading file incorrect.csv throws an error: \n" + ioe)

        self.assertEqual(len(content), 47, f"The file incorrect.csv shoudl have 47 lines after the program is executed, now it has {len(content)} lines.")

    def test_6_test_correct_content(self):
        filter_content = load(exercise, function, 'en')
        filter_content()

        content = read("correct.csv")

        corr = ["Tony;48+66;114","Emilia;23+30;53","Tuula;99-42;57","Arto;26+81;107","Antti;85+38;123","Toni;71-19;52"]
        for c in corr:
            self.assertTrue(c in content, f"After the code is executed, file correct.csv should contain a line {c} which is not found.")

    def test_7_test_incorrect_content(self):
        filter_content = load(exercise, function, 'en')
        filter_content()

        content = read("incorrect.csv")

        corr = ["Mia;93-27;38","Matti;71-7;74","Matti;80-48;6","Pekka;68-44;22","Erkki;1+90;42","Tuula;61-37;85","Antti;37+64;5","Kirsi;74-47;85"]
        for c in corr:
            self.assertTrue(c in content, f"After the code is executed, file incorrect.csv should contain a line {c} which is not found.")
              
if __name__ == '__main__':
    unittest.main()
