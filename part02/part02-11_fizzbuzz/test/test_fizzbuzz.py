import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.fizzbuzz'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def p(s):
    return "\n".join(s)

@points('2.fizzbuzz')
class FizzBuzzTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_fizz(self):
        values = "3 6 21 27 33 39 333".split(" ")
        correct = "Fizz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows:\n{}\nwhen input is {}".format(len(output), p(output), value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Output\n{}\ndoes not match with correct output\n{}\nwhen input is {}".
                    format(output[0], correct, value))

    def test_buzz(self):
        values = "5 20 35 65 550".split(" ")
        correct = "Buzz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows:\n{}\nwhen input is {}".format(len(output), p(output), value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Output\n{}\ndoes not match with correct output\n{}\nwhen input is {}".
                    format(output[0], correct, value))

    def test_fizzbuzz(self):
        values = "15 30 150 330 660".split(" ")
        correct = "FizzBuzz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)          
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))
                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows:\n{}\nwhen input is {}".format(len(output), p(output), value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Output\n{}\ndoes not match with correct output\n{}\nwhen input is {}".
                    format(output[0], correct, value))
    
if __name__ == '__main__':
    unittest.main()
