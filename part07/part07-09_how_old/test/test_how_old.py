import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.how_old'

def x(t):
    return "\n"+"\n".join(t)

@points('7.how_old')
class HowOldTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["30","12","1999"]):
           cls.module = load_module(exercise, 'en')


    def test1_uses_import_expression(self):
        with open("src/how_old.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "datetime" in cont, 
                f"Your program does not import datetime-library with the import expression.")

    def test2_test_with_older_ones(self):
        test_cases = {("1","1","1900"): "36523", ("10","9","1977"): "8147", ("30","12","1999"): 1, ("6","5","1995"): "1700"}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list(test_case)):
                try:
                    reload_module(self.module)
                except:
                    self.fail(f"Try to execute your program with the following inputs {x(test_case)}")

                output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
                lines = len(output.split("\n"))
                correct = f"You were {test_cases[test_case]} days old on the eve of the new millennium."
                msg = 'Note, that in this program no code must not be placed inside the if __name__ == "main" -block.'

                self.assertTrue(lines > 0, f"Your program does not print out anything, {msg}")

                self.assertTrue(lines == 1,                     
                    f"Your program is expected to print out 1 row, now it prints out {lines} rows: \n{output}\nwhen the input is {x(test_case)}")

                self.assertTrue(correct in output, 
                    f"Row {correct} is expected to be found out from your program, when the input is {x(test_case)}\nnow print out is \n{output}")

    def test3_test_with_younger_ones(self):
        test_cases = [("1","1","2100"), ("10","9","2019"), ("1","1","2000")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list(test_case)):
                try:
                    reload_module(self.module)
                except:
                    self.fail(f"Try to execute your program with the following inputs {x(test_case)}")

                output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
                lines = len(output.split("\n"))
                correct = "You weren't born yet on the eve of the new millennium."

                self.assertTrue(lines == 1,                     
                    f"Your program is expected to print out 1 row, now it prints out {lines} rows: \n{output}\nwhen the input is {x(test_case)}")

                self.assertTrue(correct in output, 
                    f"Row {correct} is expected to be found out from your program, when the input is {x(test_case)}\nnow print out is \n{output}")
              
if __name__ == '__main__':
    unittest.main()
