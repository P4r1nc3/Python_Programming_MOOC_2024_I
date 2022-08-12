import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.random_words'
function = "words"

def unique(lst: list):
    return len(set(lst)) == len(lst)

def equal(lst1: list, lst2: list):
    return sorted(lst1) == sorted(lst2)

def correct_items(lst: list, s: str):
    return len([x for x in lst if not x.startswith(s)]) == 0

@points('7.random_words')
class RandomWordsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[open('test/words.txt'), open('test/words.txt'),open('test/words.txt')]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        with patch('builtins.open', side_effect=[open('test/words.txt'), open('test/words.txt'),open('test/words.txt')]):
            try:
                from src.random_words import words
            except:
                self.assertTrue(False, "Your program should contain function named as words(n: int, beginning: str)")

    def test2_type_of_return_value(self):
        with patch('builtins.open', side_effect=[open('test/words.txt'), open('test/words.txt'),open('test/words.txt')]):
            try:
                from src.random_words import words
                val = words(2, "car")
                taip = str(type(val)).replace("<class '","").replace("'>","")
                self.assertTrue(type(val) == list, 
                    f"The function words is expected to return a value whichs type is list. Now it returns a value {val} whichs type is {taip} when calling the function with the parameters (2, 'car')")
            except Exception as ioe:
                self.assertTrue(False, f'Make sure, that following function call works: words(2, "car")')

    def test3_uses_import_expression(self):
        with open("src/random_words.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Your program does not import random-library with the import expression.")
    
    def test4_test_found_ones(self):
        test_cases = [(5, "car"), (4, "abs"), (7, "of"), (10, "des")]
        for test_case in test_cases:
            with patch('builtins.open', side_effect=[open('test/words.txt'), open('test/words.txt'),open('test/words.txt'), open('test/words.txt')]):
                reload_module(self.module)
                words = load(exercise, function, 'en')

                val1 = words(test_case[0], test_case[1])
                val2 = words(test_case[0], test_case[1])

                self.assertTrue(len(val1) == test_case[0], f"The list contains {len(val1)} items. It should contain {test_case[0]} items, when the parameters are {test_case}: {val1}")
                self.assertTrue(unique(val1), f"Values in the list are not unique: {val1} when the parameters were {test_case}")
                self.assertTrue(unique(val2), f"Values in the list are not unique: {val2} when the parameters were {test_case}")
                self.assertFalse(equal(val1, val2), f"Calling the function returns same values each time: {val1} When the paramaters are {test_case}")
                self.assertTrue(correct_items(val1, test_case[1]), 
                    f"All items in the list does not begin with the string {test_case[1]}: \n{val1}, \nwhen the parameters are {test_case} ")

    def test5_test_not_found_ones(self):
        test_cases = [(500, "car"), (45, "absol"), (10, "superd")]
        for test_case in test_cases:
            with patch('builtins.open', side_effect=[open('test/words.txt'), open('test/words.txt'), open('test/words.txt'), open('test/words.txt')]):
                reload_module(self.module)
                words = load(exercise, function, 'en')

                try:
                    val1 = words(test_case[0], test_case[1])
                    self.assertTrue(False, 
                        f"The function should raise ValueError with the parameters {test_case}, because there is not enough words in the file. Now the function returns {val1}.")
                except ValueError:
                    pass  
              
if __name__ == '__main__':
    unittest.main()