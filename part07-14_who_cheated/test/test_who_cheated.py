import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
import os
from shutil import copyfile

exercise = 'src.who_cheated'
function = "cheaters"

                
def format(f):
    return ", ".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def get_missing(result: list, correct: list):
    return [x for x in correct if x not in result]

def get_extra(result: list, correct: list):
    return [x for x in result if x not in correct]

filename1 = "start_times.csv"
filename2 = "submissions.csv"


@points('7.who_cheated')
class WhoCheatedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            for filename in (filename1, filename2):
                data_file = os.path.join('src', filename)
                copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
         os.remove(filename1)
         os.remove(filename2)

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
            from src.who_cheated import cheaters
        except:
            self.assertTrue(False, 'Your code should contain function named as cheaters()')
 
    def test2_type_of_return_value(self):
        cheaters = load(exercise, function, 'en')
        try:
            result = cheaters()
        except:
            self.assertTrue(False, 'An error happened during executing the function cheaters, make sure that the program works')
        
        taip = str(type(result)).replace("<class '","").replace("'>","")
        self.assertTrue(type(result) == list, f"Function cheaters is expected to return a list, now it returns a value {result} whichs type is {taip}")

    def test3_list_content(self):
        correct = ['matti', 'antti', 'henrik', 'arto', 'esko', 'kjell', 'jyrki', 'teemu', 'tiina', 'virpi', 'liisa', 'kotivalo', 'justiina', 'luukas', 'johannes']
        cheaters = load(exercise, function, 'en')
        try:
            result = cheaters()
        except:
            self.assertTrue(False, 'An error happened during executing the function cheaters, make sure that the program works')
        
        self.assertTrue(len(result) == len(correct), f"The list returned by the function is expected to contain {len(correct)} items, but now it contains {len(result)} items: {result}")
        
        missing = get_missing(result, correct)
        extra = get_extra(result, correct)

        self.assertTrue(len(missing) == 0, f"The list returned is missing the following names: {format(missing)}. Now the list was {result}")
        self.assertTrue(len(extra) == 0, f"The list returned contains the following extra names: {format(extra)}. Now the list was {result}")
        self.assertEqual(sorted(correct), sorted(result), f"The content of the list {result} does not match with the model solution {correct}")
  
if __name__ == '__main__':
    unittest.main()