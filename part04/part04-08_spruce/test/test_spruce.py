import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
import os

exercise = 'src.spruce'

def cor_spruce(height):
    lines = ["a spruce!"]
    for i in range(1, height+1):
        lines.append(" "*(height-i)+"*"*(i*2-1))

    lines.append(" "*(height-1)+"*")
    return lines

@points('4.spruce')
class SpruceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_function_exists(self):
        try:
            from src.spruce import spruce
        except:
            self.assertTrue(False, f'Your code should contain function named as spruce')
        try:
            from src.spruce import spruce
            spruce(3)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows:\rspruce(3)')



    def test_spruce_ok(self):
        for height in [3, 4, 5, 7, 10, 14, 18, 20, 25, 50]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.spruce import spruce
                spruce(height)
                output_all = get_stdout().replace(output_at_start, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l)>0 ]

                exp = cor_spruce(height)

                self.assertTrue(len(output_all)>0, f'Calling spruce({height}) does not print out anything')
                acual = '\n'.join(output)
                self.assertEqual("a spruce!", output[0].rstrip(), f'First row in the print out after calling spruce({height}) should be:\na spruce!\nbut it is:\n{output[0]}')
                self.assertEqual(len(exp), len(output), f'Calling spruce({height}) should print out {len(exp)} rows, now it prints out {len(output)} rows, the print out was\n{acual}')
                acual_spruce = "\n".join(exp)
                for i in range(len(exp)):
                    self.assertEqual(exp[i], output[i].rstrip(), f'Row {i+1} after calling spruce({height}) should be:\n{exp[i]}\nbut it is:\n{output[i]}\nBe careful with the number of spaces at the beginning of the row!\nWhole print out of the function was:\n{output_all}\nthe correct spruce:\n{acual_spruce}')

if __name__ == '__main__':
    unittest.main()