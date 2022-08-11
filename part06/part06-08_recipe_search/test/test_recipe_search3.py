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

@points('6.recipe_search_part_3')
class RecipeSearchPart3Test(unittest.TestCase):
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
            
    def test_7_search_by_ingredient_exists(self):
        with patch('builtins.input', side_effect = ["recipes1.txt"]*10):
            try:
                from src.recipe_search import search_by_ingredient
            except Exception as ioe:
                self.fail('Your code must contain a function called search_by_ingredient(filename: str, ingedient: str)')
            try:
                search_by_ingredient("test/recipes1.txt", "milk")
            except Exception as ioe:
                self.fail('Function call search_by_ingredient("test/recipes1.txt", "milk") throws an error:\n' + ioe)

    def test_8_search_by_ingredient_return_type(self):
        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_ingredient = load(exercise, function3, 'en')
            answer =  search_by_ingredient("test/recipes1.txt", "milk")
            taip = str(type(answer)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(answer) == list, f"Function {function3} should return a list, now it returns value {answer} which is of type {taip}.")

    def test_9_search_by_ingredient_1(self):
        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_ingredient = load(exercise, function3, 'en')
            answer =  search_by_ingredient("test/recipes1.txt", "milk")
            code = 'search_by_ingredient("recipes1.txt", "milk")'
            exp = """Pancakes, preparation time 15 min
Cake pops, preparation time 60 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')
        
        with patch('builtins.input', side_effect=['recipes1.txt']):
            search_by_ingredient = load(exercise, function3, 'en')
            answer =  search_by_ingredient("test/recipes1.txt", "eggs")
            code = 'search_by_ingredient("recipes1.txt", "eggs")'
            exp = """Pancakes, preparation time 15 min
Meatballs, preparation time 45 min
Cake pops, preparation time 60 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

        with patch('builtins.input', side_effect=['recipes2.txt']):
            search_by_ingredient = load(exercise, function3, 'en')
            answer =  search_by_ingredient("test/recipes2.txt", "fish")
            code = 'search_by_ingredient("recipes2.txt", "fish")'
            exp = """Almond fish, preparation time 45 min""".split('\n')

            self.assertEqual(len(exp), len(answer), f'Function returns a wrong number of recipes when called with \n{code}')
            for r in answer:
                self.assertTrue(r in exp, f'Returned wrong recipe {r} when called with {code}\nThe right return value is {exp}')
            for r in exp:
                self.assertTrue(r in answer, f'When called with {code}\nreturned recipes should contain {r}\nNow function returns {answer}')

      
if __name__ == '__main__':
    unittest.main()
