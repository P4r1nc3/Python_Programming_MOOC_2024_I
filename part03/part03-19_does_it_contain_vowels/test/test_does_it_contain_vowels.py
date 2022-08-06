import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.does_it_contain_vowels'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.does_it_contain_vowels')
class DoesItContainVowelsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a']):
            cls.module = load_module(exercise, 'en')

    def test_strings(self):
        values = ["hey", "hay","hoy", "hey", "hi", "heyah", "ahoy", "hallo", "hello", "aloha", "halloumi", "tritium", "cold", "building", "stadion", "athenaeum", "archaeology", "science", "toe", "genius"]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = [x + " found"  if (x in test_case) else (x + " not found") for x in "aeo"]
                self.assertEqual(len(output_list), len(cor), f"Your program should print out {len(cor)} row, now it prints out {len(output_list)} rows, when the input is: {test_case}")
                r = 1
                for l1,l2 in zip(cor, output_list):
                    self.assertEqual(l1.strip(), l2.strip(),
                        f"The print out in row {r} is incorrect: your program is expected to print out\n{l1}\nbut it prints out\n{l2}\nkwhen the input is {test_case}")
                    r += 1
                
if __name__ == '__main__':
    unittest.main()