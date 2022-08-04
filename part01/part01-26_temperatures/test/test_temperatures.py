import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize, remove_extra_whitespace
from functools import reduce
from random import randint

exercise = 'src.temperatures'

def close(a, b):
    return abs(a-b) < 0.001

@points('1.temperatures')
class TemperaturesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1_zero(self):
        test_input = 32
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")

            self.assertFalse(output[-1].find("Brr! It's cold in here!") > -1, "Your program printed out 'Brr! It's cold in here!' even in a case where the temperature in degrees Celsius is not below zero.")
            self.assertEqual(len(output), 1, "Your program printed out more than one row when input was 32")
            out = output[0]
            e = "32 degrees Fahrenheit equals 0.0 degrees Celsius" 
            e2= "32.0 degrees Fahrenheit equals 0.0 degrees Celsius"
            self.assertTrue(sanitize(out) == sanitize(e) or sanitize(out) == sanitize(e2), f"Your program should print out\n{e}\nwhen input is {32}, but now print out is\n{out}")
            result = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(result, 0.0), "Your program did convertion of the temperature incorrectly: result should be 0.0, but print out of your program is " + output[0])

    def test_2_positive(self):
        test_input = randint(33, 105)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertFalse(output[-1].find("Brr! It's cold in here!") > -1,
                "Your program printed out 'Brr! It's cold in here!' even in a case where the temperature in degrees Celsius is not below zero. Make sure that this does not happen with input {test_input}"
            )
            self.assertEqual(len(output), 1, "Your program printed out more than one row")
            out = output[0]
            result = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(result, correct), "Your program did not convert the temperature correctly: result with input {} should be {}, but now print out is {}".format(test_input, correct, output[0]))

    def test_3_negative(self):
        test_input = randint(-50, 31)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            out = output[0]
            result = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(result, correct), "Your program did not convert the temperature correctly: result with input {} should be {}, but now print out is {}".format(test_input, correct, output[0]))
            self.assertTrue(len(output)>1, f"Your program did not print out message 'Brr! It's cold in here!' in a case where the temperature is below zero. Make sure that this print out happens with input {test_input}")
            self.assertTrue(output[1].find("Brr! It's cold in here!") > -1, f"Your program did not print out message 'Brr! It's cold in here!' in a case where the temperature is below zero. Make sure that this print out happens with input {test_input}")
   
if __name__ == '__main__':
    unittest.main()
