import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.anagrams'
function = 'anagrams'

def get_correct(s1 : str, s2: str) -> bool:
    pass

@points('4.anagrams')
class AnagramsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')
   
    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.anagrams import anagrams
        except:
            self.assertTrue(False, 'Your code should contain function named as anagrams(string1: str, string2: str)')
        try:
            from src.anagrams import anagrams
            anagrams("house","esuoh")
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nanagrams("house","esuoh")')

    def test_2_type_of_return_value(self):
        from src.anagrams import anagrams
        val = anagrams("a","a")
        self.assertTrue(type(val) == bool, f"Calling {function} does not return value of boolean type with parameter values ('a', 'a').")
    
    def test_3_anagrams(self):
        test_cases = [("house","esuoh"), ("tar","rat"), ("stressed","desserts"), ("cat", "act"), ("save", "vase"), ("salvages", "lasvegas"), ("state","taste"), ("python","nythop")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                from src.anagrams import anagrams
                
                correct = True
                test_result = anagrams(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} with test input {test_case}.")

    def test_4_non_anagrams(self):
        test_cases = [("house","mouse"), ("tree","three"), ("desserts","reindeers"), ("test","set"), ("python","java")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                from src.anagrams import anagrams
                
                correct = False
                test_result = anagrams(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} with test input {test_case}.")
                
if __name__ == '__main__':
    unittest.main()
