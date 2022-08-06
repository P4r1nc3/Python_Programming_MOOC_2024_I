import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.longer_string'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.longer_string')
class LongerStringTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a', 'b']):
            cls.module = load_module(exercise, 'en')

    def test_first_one_is_longer(self):
        values = [("rabbit", "duck"), ("python", "java"), ("popcorn", "candy"), ("superman", "zorro")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works correctly with the input {test_case}")
                out = get_stdout()
                output = out.split("\n")  
                corr = test_case[0] + " is longer"
                self.assertTrue(len(out) > 0, "Your program does not print out anything with the inputs {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Your program should print out only one row in addtion to asking for the inputs from the user, your program's print out is now in {len(output)} rows.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"The print out is incorrect with the inputs {test_case}: your program's print out is\n{out}\nwhen correct print out is\n{corr}")

    def test_second_one_is_longer(self):
        values = [("first", "second"), ("short", "longer"), ("test", "testing"), ("xyz", "abcd")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works correctly with the input {test_case}")
                out = get_stdout()
                output = out.split("\n")
                corr = test_case[1] + " is longer"
                self.assertTrue(len(out) > 0, "Your program does not print out anything with the inputs {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Your program should print out only one row in addtion to asking for the inputs from the user, your program's print out is now in {len(output)} rows.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"The print out is incorrect with the inputs {test_case}: your program's print out is\n{out}\nwhen correct print out is\n{corr}")

    def test_equal_length(self):
        values = [("tik", "tok"), ("jack", "lisa"), ("abcd", "abcd"), ("sweet", "candy")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                corr = "The strings are equally long"
                self.assertTrue(len(out) > 0, "Your program does not print out anything with the inputs {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Your program should print out only one row in addtion to asking for the inputs from the user, your program's print out is now in {len(output)} rows.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"The print out is incorrect with the inputs {test_case}: your program's print out is\n{out}\nwhen correct print out is\n{corr}")

if __name__ == '__main__':
    unittest.main()