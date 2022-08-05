import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.input_validation'

def p(a):
    return "\n".join(a)

@points('2.input_validation')
class InputValidationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["0"]):
            cls.module = load_module(exercise, 'en')

    def test_1_termination(self):
        values = "1 0".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure that execution of your program stops with the input:\n{p(values)}")

    def test_2_numbers_and_termination(self):
        values = "9 4 16 1 0".split(" ")
        correct = "3.0\n2.0\n4.0\n1.0\nExiting..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, f"Your program does not print out anything with the input\n:{p(values)}")
            
            self.assertTrue(len(output.split("\n")) == 5, "Instead of five rows, your program's output is in {} rows\n{}\nwhen input is\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{} \ndoes not match with the correct output\n{} \nwhen input is\n{}".
                format(output, correct, p(values)))

    def test_3_invalid(self):
        values = "-1 0".split(" ")

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure that execution of your program stops with the input:\n{p(values)}")

    def test_4_numbers_invalid_number_and_termination(self):
        values = "9 4 16 -1 0".split(" ")
        correct = "3.0\n2.0\n4.0\nInvalid number\nExiting..."

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input:\n{}".format(p(values)))

            output = get_stdout()
            self.assertTrue(len(output)>0, f"Your program does not print out anything with the input\n:{p(values)}")
            self.assertTrue(len(output.split("\n")) == 5, "Instead of printing out five rows in addition to asking for the inputs from the user, your program's print out is in {} rows:\n{}\nwhen input is\n{}".
                format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{} \ndoes not match with the correct output\n{} \nwhen input is\n{}".
                format(output, correct, p(values)))

    def test_5_termination_only(self):
        values = "0".split(" ")
        correct = "Exiting..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, f"Your program does not print out anything with the input {p(values)}")
            self.assertTrue(len(output.split("\n")) == 1, "Instead of printing out one row in addition to asking for the inputs from the user, your program's print out is in {} rows:\n{}\nwhen input is\n{}".
                format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{} \ndoes not match with the correct output\n{} \nwhen input is\n{}".
                format(output, correct, p(values)))

if __name__ == '__main__':
    unittest.main()