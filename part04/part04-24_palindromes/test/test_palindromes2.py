import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap

exercise = 'src.palindromes'
function = 'palindromes'

def get_correct(test_case: list) -> list:
    pass


@points('4.palindromes')
class PalindromestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["aa"]):
           cls.module = load_module(exercise, 'en')

    def test_5_inputs_2(self):
        test_cases = "one two third fourth neveroddoreven".split()
        correct = ["that wasn't a palindrome"] * 4
        correct.append("neveroddoreven is a palindrome!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ") for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)
            ntest_cases = '\n'.join(test_cases)
            self.assertTrue(correct == output, f"The print out\n{noutput}\ndoes not match with the model solution:\n{ncorrect}\nwith the following test input:\n{ntest_cases}")

    def test_6_syotteet3(self):
        test_cases = "aaabaa bbbcb ccccdccc xyzzzxyz abcdcba".split()
        correct = ["that wasn't a palindrome"] * 4
        correct.append("abcdcba is a palindrome!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ")  for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)
            ntest_cases = '\n'.join(test_cases)    
            self.assertTrue(correct == output, f"The print out\n{noutput}\ndoes not match with the model solution:\n{ncorrect}\nwith the following test input:\n{ntest_cases}")
                 
if __name__ == '__main__':
    unittest.main()