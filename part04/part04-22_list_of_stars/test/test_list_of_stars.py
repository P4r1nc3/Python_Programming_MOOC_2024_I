import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.list_of_stars'
function = 'list_of_stars'

def get_correct(lst: list) -> str:
    return "\n".join(["*" * x for x in lst])

@points('4.list_of_stars')
class ListOfStarsTest(unittest.TestCase):
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
            from src.list_of_stars import list_of_stars
        except:
            self.assertTrue(False, 'Your code should contain function named as list_of_stars(numbers: list)')
        try:
            from src.list_of_stars import list_of_stars
            list_of_stars([1])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows \nlist_of_stars([1])')

    def test_2_type_of_return_value(self):
        from src.list_of_stars import list_of_stars
        val = list_of_stars([1])
        self.assertTrue(val == None, f"Calling {function} should not return anything, now it returns value which type is {type(val)}")
    
    def test_3_numbers_0(self):
        test_case = [2,2]
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            reload_module(self.module)
            from src.list_of_stars import list_of_stars
            list_of_stars(test_case)
            
            correct = get_correct(test_case)

            output_at_start = get_stdout()
            list_of_stars(test_case)
            output = get_stdout().replace(output_at_start+'\n', '', 1)

            c_rows = len(correct.split('\n'))
            r_rows = len(output.split('\n'))
            self.assertTrue(len(output)>0, f"Your function does not print out anything when it is called as follows:\nlist_of_stars({test_case})")
            self.assertEqual(c_rows, r_rows, f"The amount of the rows printed out is incorrect with the test input {test_case}. Your function printed out {r_rows} rows, correct amount is {c_rows}. The print out was:\n{output}\nit was expected to be:\n{correct}\nbe careful that you do not print out empty extra rows!")
            self.assertEqual(correct, output, f"The result: \n{output}\ndoes not match with the model solution\n{correct}\nwith the test input {test_case}.")

if __name__ == '__main__':
    unittest.main()