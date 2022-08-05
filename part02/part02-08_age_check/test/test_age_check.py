import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.age_check'

@points('2.age_check')
class AgeCheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'en')

    def test_1_five_and_over(self):
        values = "5 6 11 23 52 80".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's out is in {} rows with input {}".format(len(output), value))
                self.assertTrue(output[0].find("Ok, you're") > -1, "From output\n{}\nstring 'Ok, you're' is not found when input is {}".
                    format(output[0], value))
                self.assertTrue(output[0].find(value + " years old") > -1, "From output\n{}\nstring {} is not found when input is {}".
                    format(output[0], value + " years old", value))

    def test_2_zero_to_five(self):
        values = "0 1 4".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's out is in {} rows with input {}".format(len(output), value))
                self.assertTrue(output[0].find("I suspect you can't write quite yet") > -1, "From output\n{}\nstring {} is not found when input is {}".
                    format(output[0], "I suspect you can't write quite yet", value))

    def test_3_under_zero(self):
        values = "-1 -5 -11 -902".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's out is in {} rows with input {}".format(len(output), value))
                self.assertTrue(output[0].find("That must be a mistake") > -1, "From output\n{}\nstring {} is not found when input is {}".
                    format(output[0], "That must be a mistake", value))
                
if __name__ == '__main__':
    unittest.main()
