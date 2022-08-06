import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.end_to_beginning'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.end_to_beginning')
class EndToBeginningTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a']):
            cls.module = load_module(exercise, 'en')

    def test_strings(self):
        values = ["abc", "hiya", "monkey", "teststring", "programming"]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works with the input {test_case}")
                output = get_stdout()
                output_list = output.split("\n")
                cor = [x for x in test_case[::-1]]
                self.assertEqual(len(output_list), len(cor), f"Your program is expected to print out {len(cor)} rows, now your program's print out is in {len(output_list)} rows.")
                r = 1
                for l1,l2 in zip(cor, output_list):
                    self.assertTrue(sanitize(l1) == sanitize(l2), f"When the input is {test_case} print out in row {r+1} is incorrect, row should be\n{l1}\nbut it is\n{l2}")
    
if __name__ == '__main__':
    unittest.main()