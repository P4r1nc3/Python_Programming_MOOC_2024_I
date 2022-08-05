import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.repeat_password'

@points('2.repeat_password')
class RepeatPasswordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["secret"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        values = "secret secret".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input {}".format(values))

    def test_1(self):
        with patch('builtins.input', side_effect= ["sekred", "sekred", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["sekred", "sekred"])

            expected = 'User account created!'
            self.assertFalse(len(output) == 0 , f"With the input\n{inpt}\nyour program should print out\n{expected}\nnow your program does not print out anything" )
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input:\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

    def test_2(self):
        with patch('builtins.input', side_effect= ["sekred", "wrong", "sekred", AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["sekred", "wrong", "sekred"])

            expected = 'They do not match!\nUser account created!'
            self.assertEqual(sanitize(expected), sanitize(output), f"With the input:\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

    def test_moar(self):
        for wrongs in [3, 4, 7, 11, 23]: 
            
            with patch('builtins.input', side_effect= ["sekred"] + ["wrong"]* wrongs + ["sekred", AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  

                inpt = '\n'.join(["sekred"] + ["wrong"]* wrongs + ["sekred"]) 

                expected = '\n'.join(["They do not match!"]*wrongs + ["User account created!"])
                self.assertEqual(sanitize(expected), sanitize(output), f"With the input:\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

if __name__ == '__main__':
    unittest.main()