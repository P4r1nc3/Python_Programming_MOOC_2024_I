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

exercise = 'src.who_cheated_2'
function = "final_points"

                
def format(f):
    return ",".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def get_incorrect(result: dict, correct: dict):
    inc = {}
    for name in correct:
        if name not in result:
            inc[name] = correct[name]
        elif correct[name] != result[name]:
            inc[name] = correct[name]
    return inc


filename1 = "start_times.csv"
filename2 = "submissions.csv"


@points('7.who_cheated_2')
class WhoCheated2(unittest.TestCase):
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
            from src.who_cheated_2 import final_points
        except:
            self.assertTrue(False, 'Your code should contain function named as final_points()')
 
    def test2_type_of_return_value(self):
        final_points = load(exercise, function, 'en')
        try:
            result = final_points()
        except:
            self.assertTrue(False, 'An error happened during executing the function final_points, make sure that the program works')
        
        taip = str(type(result)).replace("<class '","").replace("'>","")
        self.assertTrue(type(result) == dict, f"Function final_points is expected to return a dictionary, now it returns a value {result} whichs type is {taip}")

    def test3_list_content(self):
        correct = {'matti': 43, 'erkki': 45, 'antti': 41, 'emilia': 42, 'henrik': 37, 'arto': 40, 'esko': 45, 'kjell': 47, 'jyrki': 41, 'teemu': 43, 'tiina': 36, 'jenna': 38, 'virpi': 39, 'kalle': 46, 'maija': 40, 'uolevi': 34, 'anna': 45, 'liisa': 42, 'kotivalo': 43, 'justiina': 44, 'matteus': 30, 'markus': 35, 'luukas': 40, 'johannes': 39}
        final_points = load(exercise, function, 'en')
        try:
            result = final_points()
        except:
            self.assertTrue(False, 'An error happened during executing the function final_points, make sure that the program works')
        
        self.assertTrue(len(result) == len(correct), f"The dictionary returned by the function is expected to contain {len(correct)} items, but now it contains {len(result)} items: {result}")
        
        wrong = get_incorrect(result, correct)

        self.assertTrue(len(wrong) == 0, f"Following items were incorrect or missing from the dictionary: {wrong}. Now dictionary was {result} and correct answer is {correct}")
        self.assertEqual(correct, result, f"The content of the dictionary {format(result)} does not match with the model solution {format(correct)}")

if __name__ == '__main__':
    unittest.main()