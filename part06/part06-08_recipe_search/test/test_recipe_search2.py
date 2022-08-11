import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
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

@points('6.recipe_search_part_2')
class RecipeSearchPart2Test(unittest.TestCase):
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

    def test_4_search_by_time_exists(self):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            try:
                from src.recipe_search import search_by_time
            except Exception as ioe:
                self.fail('Your code must contain a function called search_by_time(filename: str, time: int)')
            try:
                search_by_time("test/recipes1.txt", 1)
            except Exception as ioe:
                self.fail('Function call search_by_time("test/recipes1.txt", 1) throws an error:\n' + ioe)

    def test_5_search_by_time_return_type(self):
        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_time = load(exercise, function2, 'en')
            answer = search_by_time("test/recipes1.txt", 20)
            taip = str(type(answer)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(answer) == list, f"Function {function2} should return a list, now it returns value {answer} which is of type {taip}.")

    def test_6_search_by_time_1(self):
        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_time = load(exercise, function2, 'en')
            answer = search_by_time("test/recipes1.txt", 20)
            code = 'search_by_time("recipes1.txt", 20)'
            exp = """Pancakes, preparation time 15 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_time = load(exercise, function2, 'en')
            answer = search_by_time("test/recipes1.txt", 35)
            code = 'search_by_time("recipes1.txt", 35)'
            exp = """Pancakes, preparation time 15 min
Tofu rolls, preparation time 30 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

        with patch('builtins.input', side_effect=['recipes2.txt']):
            search_by_time = load(exercise, function2, 'en')
            answer = search_by_time("test/recipes2.txt", 10)
            code = 'search_by_time("recipes2.txt", 10)'
            exp = """Oat porridge, preparation time 6 min
Strawberry trifle, preparation time 2 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

      

if __name__ == '__main__':
    unittest.main()
