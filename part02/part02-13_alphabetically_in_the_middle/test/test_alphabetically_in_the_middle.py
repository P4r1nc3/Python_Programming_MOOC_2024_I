import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.alphabetically_in_the_middle'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.alphabetically_in_the_middle')
class AlphabeticallyInTheMiddleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['A','B',"C"]):
            cls.module = load_module(exercise, 'en')

    def test_middle_first(self):
        values = ["Y X Z", "B C A", "R U C", "H D N"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(valuegroup))

                correct = "The letter in the middle is " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], correct, format_tuple(valuegroup)))

    def test_middle_second(self):
        values = ["x y z", "c b a", "p d b", "e w y"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(valuegroup))

                correct = "The letter in the middle is " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], correct, format_tuple(valuegroup)))

    def test_middle_third(self):
        values = ["X Z Y", "e a c", "l a f", "b x r"]
        for letters in values:
            valuegroup = letters.split(" ")
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(valuegroup))

                correct = "The letter in the middle is " + sorted(valuegroup)[1]
                
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(correct) > -1, "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is {}".
                    format(output[0], correct, format_tuple(valuegroup))) 

if __name__ == '__main__':
    unittest.main()
