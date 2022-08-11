import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.read_input'
function = 'read_input'


@points('6.read_input')
class ReadInputTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=list(range(1000))):
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
            from src.read_input import read_input
        except:
            self.fail('Your code should contain function read_input(prompt: str, lower_limit: int, upper_limit: int)')

    def test_2_ok_numbers(self):
        with patch('builtins.input', side_effect=["7"]):
            read_input = load(exercise, function, 'en')
            try:
                result = read_input("Enter a number:", 2, 10)
            except:
                self.fail('Ensure that the function can be called like this: read_input("Enter a number:", 2, 10)')

            self.assertEqual(result, 7, "Function should return value 7 when user enters 7")

    def test_3_too_small1(self):
        with patch('builtins.input', side_effect=["4","6"]):
            read_input = load(exercise, function, 'en')
            result = read_input("Enter a number", 5, 10)
            output = get_stdout()
            self.assertTrue("You must type in an integer between 5 and 10" in output,
                "Function should give an error message \n'You must type in an integer between 5 and 10'\n, when it's called as read_input('Enter a number', 5, 10) and the value entered is < 5.")
            self.assertEqual(result, 6, f"Function should return value 6 when user enters\n4\n6\nand the function is called with arguments ('Enter a number', 5, 10). Now the function returns {result}")

    def test_3_too_small2(self):
        with patch('builtins.input', side_effect=["2","4","6"]):
            read_input = load(exercise, function, 'en')
            result = read_input("Enter a number", 5, 10)
            output = get_stdout()
            self.assertTrue("You must type in an integer between 5 and 10" in output,
                "Function should give an error message \n'You must type in an integer between 5 and 10'\n, when it's called as read_input('Enter a number', 5, 10) and the value entered is < 5.")
            self.assertEqual(result, 6, f"Function should return value 6 when user enters\n2\n4\n6\nand the function is called with arguments ('Enter a number', 5, 10). Now the function returns {result}")

    def test_4_too_large1(self):
         with patch('builtins.input', side_effect="6 10 7 30 40 4".split()):
            read_input = load(exercise, function, 'en')
            result = read_input("Enter a number", 1, 5)
            output = get_stdout()
            self.assertTrue("You must type in an integer between 1 and 5" in output,
                "Function should give an error message \n'You must type in an integer between 1 and 5'\n, when it's called as read_input('Enter a number', 1, 5) and the value entered is > 5.")
            self.assertEqual(result, 4, f"Function should return value 4 when user enters\n6\n10\n7\n30\n40\n4\nand the function is called with arguments ('Enter a number', 1, 5). Now the function returns {result}")

    def test_5_no_numbers(self):
        with patch('builtins.input', side_effect=["one","two","three","100"]):
            read_input = load(exercise, function, 'en')
            try:
                result = read_input("Give a number:", 95, 105)
            except:
                self.fail("Ensure that your program can be execute with input values\none\ntwo\nthree\n100")
            output = get_stdout()
            self.assertTrue("You must type in an integer between 95 and 105" in output,
                "Function should give an error message \n'You must type in an integer between 95 and  105', when its called with parameters ('Give a number', 95, 105) and the input contains letters only.")
            self.assertEqual(result, 100, f"Function should return value 100 when user enters 100 and the function is called with arguments ('Enter a number', 95, 105). Now the function returns {result}")

if __name__ == '__main__':
    unittest.main()
