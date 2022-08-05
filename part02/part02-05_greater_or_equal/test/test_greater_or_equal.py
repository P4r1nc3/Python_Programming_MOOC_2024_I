import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.greater_or_equal'

def format_tuple(d : tuple):
    return f"{d[0]}, {d[1]}"

@points('2.greater_or_equal')
class GreaterOrEqualTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0']):
            cls.module = load_module(exercise, 'en')

    def test_first_one_is_greater(self):
        values = [("5","1"), ("100", "0"), ("99","-99"), ("155","154"), ("211","23")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out)>0, "Your program does not print out anything with input {}".format(format_tuple(valuepair)))
            
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows with input {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find(valuepair[0]) > -1, "From ouput\n{}\nthe greater number {} is not found when input is {}".format(output[0], valuepair[0], format_tuple(valuepair)))
    
    def test_second_one_is_greater(self):
        values = [("0","1"), ("100", "120"), ("-99","99"), ("151","1534"), ("23","211")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out)>0, "Your program does not print out anything with input {}".format(format_tuple(valuepair)))
            
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows with input {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find(valuepair[1]) > -1, "From ouput\n{}\nthe greater number {} is not found when input is {}".format(output[0], valuepair[1], format_tuple(valuepair)))

    def test_equal_ones(self):
        values = [("1","1"), ("100", "100"), ("-99","-99"), ("0","0")]
        for valuepair in values:
            with patch('builtins.input', side_effect = list(valuepair)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")

                self.assertTrue(len(out)>0, "Your program does not print out anything with input {}".format(format_tuple(valuepair)))
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows with input {}".format(len(output), format_tuple(valuepair)))
                self.assertTrue(output[0].find("equal") > -1, "From output\n{}\nword 'equal' is not found when input is {}".format(output[0], format_tuple(valuepair)))
   
if __name__ == '__main__':
    unittest.main()
