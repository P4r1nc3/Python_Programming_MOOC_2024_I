import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.fix_syntax'

def p(a):
    return "\n".join(a)

@points('2.fix_syntax')
class FixSyntaxTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'en')

    def test_over_hundred_0(self):
        value = 101
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "Make sure that you can run the program with input {}".format(value))

    def test_under_hundred_0(self):
        value = 90
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "Make sure that you can run the program with input {}".format(value))

    def test_under_hundred_1(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Instead of two rows, your program's output is in {} rows with input {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Output does not contain correct number {} with input {}. Your program printed out\n{}".format(value, value, p(output)))
            model = str(value) + " must be my lucky number!"
            self.assertEqual(sanitize(output[0]), model, "First row of the output does not match with the model solution {} with input {}. Your program printed out\n{}".format(model, value, p(output)))
            model = "Have a nice day!"
            self.assertEqual(sanitize(output[1]), model, "Second row of the output does not match with the model solution {} with input {}. Your program printed out\n{}".format(model, value, p(output)))
            
    def test_under_hundred_2(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Instead of two rows, your program's output is in {} rows with input {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Output does not contain correct number {} with input {}. Your program printed out\n{}".format(value, value, p(output)))
            model = str(value) + " must be my lucky number!"
            self.assertEqual(sanitize(output[0]), model, "First row of the output does not match with the model solution {} with input {}. Your program printed out\n{}".format(model, value, p(output)))
            model = "Have a nice day!"
            self.assertEqual(sanitize(output[1]), model, "Second row of the output does not match with the model solution {} with input {}. Your program printed out\n{}".format(model, value, p(output)))
            
    def test_over_hundred_1(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Instead of five rows, your program's output is in {} rows with input {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Subtracted number {} is not found from the output with input {}. Your program printed out\n{}".format(value - 100, value, p(output)))
            self.assertEqual(sanitize(output[0]), "The number was greater than one hundred", "First row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[1]), "Now its value has decreased by one hundred", "Second row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[3]), str(value - 100) + " must be my lucky number!", "Fourth row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[4]), "Have a nice day!", "Fifth row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))

    def test_over_hundred_2(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Instead of five rows, your program's output is in {} rows with input {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Subtracted number {} is not found from the output with input {}. Your program printed out\n{}".format(value - 100, value, p(output)))
            self.assertEqual(sanitize(output[0]), "The number was greater than one hundred", "First row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[1]), "Now its value has decreased by one hundred", "Second row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[3]), str(value - 100) + " must be my lucky number!", "Fourth row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[4]), "Have a nice day!", "Fifth row of the output does not match with the model solution with input {}. Your program printed out\n{}".format(value, p(output)))
    
if __name__ == '__main__':
    unittest.main()
