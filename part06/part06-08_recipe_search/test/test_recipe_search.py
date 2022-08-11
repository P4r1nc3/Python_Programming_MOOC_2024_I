import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.recipe_search'

def f(d):
    return '\n'.join(d)

function1 = "search_by_name"
function2 = "search_by_time"
function3 = "search_by_ingredient"

testdata = ["recipes1.txt", "recipes2.txt"]

import os
from shutil import copyfile

@points('6.recipe_search_part_1')
class RecipeSearchPart1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)               
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be included inside
if __name__ == "__main__":
block. The following code needs to be relocated::
"""
        self.assertTrue(ok, message+line)

    def test_1_function_search_by_name_exists(self):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            try:
                from src.recipe_search import search_by_name
            except Exception as ioe:
                self.fail('Your code must contain a function called search_by_name(filename: str, word: str)')
            try:
                search_by_name("test/recipes1.txt", "bun")
            except Exception as ioe:
                self.fail('Function call search_by_name("test/recipes1.txt", "bun") throws an error:\n' + ioe)

    def test_2_search_by_name_return_type(self):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            search_by_name = load(exercise, function1, 'en')
            val = search_by_name("test/recipes1.txt", "bun")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == list, f"Function {function1} should return a list, now it returns value {val} which is of type {taip}.")

    def test_3_search_by_name_1(self):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            search_by_name = load(exercise, function1, 'en')
            answer = search_by_name("test/recipes1.txt", "cake")
            code = 'search_by_name("recipes1.txt", "cake")'
            exp = """Pancakes
Cake pops""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            search_by_name = load(exercise, function1, 'en')
            answer = search_by_name("test/recipes1.txt", "lls")
            code = 'search_by_name("recipes1.txt", "lls")'
            exp = """Meatballs
Tofu rolls""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

        with patch('builtins.input', side_effect = ["recipes2.txt"]*10):
            search_by_name = load(exercise, function1, 'en')
            answer = search_by_name("test/recipes2.txt", "oat")
            code = 'search_by_name("recipes2.txt", "oat")'
            exp = ["Oat porridge"]

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')



if __name__ == '__main__':
    unittest.main()
