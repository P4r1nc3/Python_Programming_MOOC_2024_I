import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.leap_year'

@points('2.leap_year')
class LeapYearTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_divisible_by_four(self):
        values = "4 16 1204 1616 1976 2008".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("is a leap year") > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], "That year is a leap year.", value))

    def test_not_divisible_by_four(self):
        values = "5 19 1307 1753 1975 2039".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("is not a leap year") > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], "That year is not a leap year.", value))

    def test_divisible_by_four_hundred(self):
        values = "400 800 1600 2000 2400".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("is a leap year") > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], "That year is a leap year.", value))
    
    def test_divisible_by_one_hundred_not_by_four_hundred(self):
        values = "500 700 1100 1300 1900".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("is not a leap year") > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], "That year is not a leap year.", value))
    
if __name__ == '__main__':
    unittest.main()
