import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.shall_we_continue'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def p(a):
    return "\n".join(a)

@points('2.shall_we_continue')
class ShallWeContinueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["no"]):
            cls.module = load_module(exercise, 'en')

    def test_1_first(self):
        values = "continue no".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input {}".format(values))

    def test_2_one_and_no(self):
        values = "what no".split(" ")
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) > 0, "Your program does not print out anything with the input:\n{}".format(p(values)))

            correct = "hi\nhi\nokay then"
            
            self.assertTrue(len(output.split("\n")) == 3, "Instead of three rows, your programs output is in {} rows: \n{}\nwhen input is:\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is:\n{}".
                format(output, correct, p(values)))


    def test_3_three_and_no(self):
        values = "continue yeah yes no".split(" ")
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) > 0, "Your program does not print out anything with the input:\n{}".format(p(values)))
            correct = "hi\nhi\nhi\nhi\nokay then"
            
            self.assertTrue(len(output.split("\n")) == 5, "Instead of five rows, your programs output is in {} rows: \n{}\nwhen input is:\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is:\n{}".
                format(output, correct, p(values)))

    def test_4_only_no(self):
        values = ["no"]
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) > 0, "Your program does not print out anything with the input:\n{}".format(p(values)))
            correct = "hi\nokay then"
            
            self.assertTrue(len(output.split("\n")) == 2, "Instead of two rows, your programs output is in {} rows: \n{}\nwhen input is:\n{}".format(len(output.split("\n")), output, p(values)))
            self.assertTrue(sanitize(output) == sanitize(correct), "Output\n{}\ndoes not match with the correct output\n{}\nwhen input is:\n{}".
                format(output, correct, p(values)))
    
if __name__ == '__main__':
    unittest.main()
