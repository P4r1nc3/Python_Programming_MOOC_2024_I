import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.age_of_maturity'

@points('2.age_of_maturity')
class AgeOfMaturityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'en')

    def test_1_adults(self):
        values = "18 24 96 102".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out) >0, "Your program does not print out anything with input {}".format(value))
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows with input {}".format(len(output), value))
                self.assertEqual(output[0].strip(), f"You are of age!", f"With input {value} output should be\nYou are of age!\nnow it is\n" + output[0])

    def test_2_underages(self):
        values = "17 11 8 3".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out) >0, "Your program does not print out anything with input {}".format(value))
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows with input {}".format(len(output), value))
                self.assertEqual(output[0].strip(), "You are not of age!", f"With input {value} output shoud be\nYou are not of age!\nnow it is\n" + output[0])
   
if __name__ == '__main__':
    unittest.main()
