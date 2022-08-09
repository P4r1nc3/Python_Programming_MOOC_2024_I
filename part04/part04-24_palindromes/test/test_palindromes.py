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
class PalindromesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["aa"]):
           cls.module = load_module(exercise, 'en')

    def test_1_function_exists(self):
        try:
            from src.palindromes import palindromes
        except:
            self.assertTrue(False, 'Your code should contain function named as palindromes(word: str)')
        try:
            from src.palindromes import palindromes
            palindromes("abba")
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\npalindromes("abba")')

    def test_2_type_of_return_value(self):
        from src.palindromes import palindromes
        val = palindromes("aa")
        self.assertTrue(type(val) == bool, f"Calling {function} does not return value of boolean type with parameter value 'aa'.")
    
    def test_3_function(self):
        from src.palindromes import palindromes
        test_cases = {"abba" : True, "abccba" : True, "neveroddoreven" : True, "neveroddorevener" : False, "abbab": False, "abcabc" : False, "okok" : False}
        for test_case in test_cases:
            correct = test_cases[test_case]
            test_result = palindromes(test_case)

            self.assertTrue(correct == test_result, f'The result of function {test_result} does not match with the model solution {correct} when calling palindromes("{test_case}")')

    def test_4_inputs(self):
        test_cases = "okay no hiya ellohello mom".split()
        correct = ["that wasn't a palindrome"] * 4
        correct.append("mom is a palindrome!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ") for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)

            ntest_cases = '\n'.join(test_cases)

            mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
            #\n{mssage}")   
            self.assertFalse(len(noutput)==0, f"Your program does not print out anything with the test input\n{ntest_cases}\n{mssage}")
            self.assertTrue(correct == output, f"The print out\n{noutput}\ndoes not match with the model solution:\n{ncorrect}\nwith the test input:\n{ntest_cases}")
     
if __name__ == '__main__':
    unittest.main()