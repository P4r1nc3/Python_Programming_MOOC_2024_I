import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.pin_and_number_of_attempts'

def p(a):
    return "\n".join(a)

@points('2.pin_and_number_of_attempts')
class PinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["4321"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        values = "4321".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input\n{}".format(p(values)))

    def test_1(self):
        with patch('builtins.input', side_effect= ["4321", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["4321"])

            expected = 'Correct! It only took you one single attempt!'
            self.assertFalse(len(output) == 0 , f"With the input\n{inpt}\nyour program should print out:\n{expected}\nnow your progam does not print out anything" )
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

    def test_2(self):
        with patch('builtins.input', side_effect= ["1234", "4321", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["1234", "4321"])

            expected = 'Wrong\nCorrect! It took you 2 attempts'
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

    def test_moar(self):
        for wrongs in [3, 4, 7, 11, 23]: 
            
            with patch('builtins.input', side_effect= ["0000"]* wrongs + ["4321", AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  

                inpt = '\n'.join(["0000"]* wrongs + ["4321"]) 

                expected = '\n'.join(["Wrong"]*wrongs + ["Correct! It took you "+str(wrongs+1)+" attempts"])
                self.assertEqual(sanitize(expected), sanitize(output), f"With the input\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

if __name__ == '__main__':
    unittest.main()
