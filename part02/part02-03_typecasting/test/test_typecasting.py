import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.typecasting'

@points('2.typecasting')
class TypecastingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'en')

    def test_numbers(self):
        values = "0.1 1.34 101.001 12.474747".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                intpart = value[:value.find(".")]
                decpart = "0" + value[value.find(".") :]
                reload_module(self.module)
                acual_output = get_stdout()
                output = acual_output.split("\n")
            
                self.assertTrue(len(acual_output)>0, "Your program does not print out anything with input {}".format(value))
                self.assertTrue(len(output) == 2, "Instead of two rows, your program's output is in {} rows with input {}".format(len(output), value))
                self.assertTrue(output[0].find(str(intpart)) > -1, "Correct integer part {} is not found from output {} with input {}".format(intpart, output[0], value))
                self.assertTrue(output[1].find(str(decpart)) > -1, "Correct decimal part {} is not found from output {} with input {}".format(decpart, output[0], value))
   
if __name__ == '__main__':
    unittest.main()