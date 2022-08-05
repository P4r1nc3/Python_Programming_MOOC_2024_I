import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.elder'

def format_tuple(d : tuple):
    return '\n'.join(list(d))
    
def p(a):
    return "\n".join(a)

@points('2.elder')
class ElderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0','0','0']):
            cls.module = load_module(exercise, 'en')

    def test_first_one_is_elder(self):
        values = [("Jeremy","20","Amy","19"), ("Paula","29","Patrick","16"), ("Mike","54","Maja","49"), ("Anna","23","Maja","9")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"Make sure that your program works with input\n{format_tuple(valuegroup)}")
                    pass

                # Remove headers
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Person") ]

                self.assertFalse(len(output) == 0, "Your program does not print out anything with input:\n{}".
                    format(format_tuple(valuegroup)))
                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), p(output), format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "From output\n{}\nthe name of the elder person {} is not found, when input is:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))
                self.assertFalse(output[0].find(valuegroup[2]) > -1, "From output\n{}\nthe name of the younger person was found {} when input was:\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))

    def test_second_one_is_elder(self):
        values = [("Lena","20","Peter","39"), ("Simon","29","Andreas","46"), ("Alma","1","Margareth","49"), ("Maja","9","Anna","23")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Remove headers
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Person") ] 

                self.assertFalse(len(output) == 0, "Your program does not print out anything with input:\n{}".
                    format(format_tuple(valuegroup)))
                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), p(output), format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[2]) > -1, "From output\n{}\nthe name of the elder person {} is not found, when input is:\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))
                self.assertFalse(output[0].find(valuegroup[0]) > -1, "From output\n{}\nthe name of the younger person was found {} when input was:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))

    def test_same_age(self):
        values = [("Larry","20","Peter","20"), ("Simeon","11","Li","11")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Remove headers
                out = [x for x in get_stdout().split("\n") if len(x)>0 ]
                output = [x for x in out if not x.startswith("Person") ]
                
                self.assertFalse(len(output) == 0, "Your program does not print out anything with input:\n{}".
                    format(format_tuple(valuegroup)))
                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), p(output), format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "From output\n{}\nname {} is not found when input is:\n{}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[2]) > -1, "From output\n{}\nname {} is not found when input is:\n{}".
                    format(output[0], valuegroup[2], format_tuple(valuegroup)))
                self.assertTrue(output[0].find("same age") > -1, "Output\n{}\ndoes not contain mention 'same age'".format(output[0]))
        
if __name__ == '__main__':
    unittest.main()
