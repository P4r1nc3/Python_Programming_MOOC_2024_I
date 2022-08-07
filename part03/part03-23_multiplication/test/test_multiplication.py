import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.multiplication'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('3.multiplication')
class MultiplicationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['2']):
            cls.module = load_module(exercise, 'en')

    def test_multiplication(self):
        values = [2, 3, 4]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = []    
                for i in range(1, int(test_case) + 1):
                    for j in range(1, int(test_case) + 1):
                        cor.append(f"{i} x {j} = {i*j}")
                self.assertEqual(len(output_list), len(cor), f"Your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows, when the input is {test_case}.")
                r = 1
                cccc = "\n".join(cor)
                for l1,l2 in zip(cor, output_list):
                    self.assertTrue(sanitize(l1) == sanitize(l2), 
                        f"The print out in the row {r} is incorrect: your program should print out\n{cccc}\nbut it prints out\n{output}\nwhen the input is {test_case}")
                    r += 1

if __name__ == '__main__':
    unittest.main()