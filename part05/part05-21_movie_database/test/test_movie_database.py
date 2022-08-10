import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.movie_database'
function = 'add_movie'

def get_correct() -> dict:
    pass

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.movie_database')
class MovieDatabaseTest(unittest.TestCase):
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
            from src.movie_database import add_movie
        except:
            self.assertTrue(False, 'Your code should contain function named as add_movie(database: list, name: str, director: str, year: int, runtime: int)')
        try:
            add_movie = load(exercise, function, 'en')
            add_movie([], "", "", 1, 1)
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nadd_movie([], "", "", 1, 1)')


    def test_2_type_of_return_value(self):
        add_movie = load(exercise, function, 'en')
        val = add_movie([], "", "", 1, 1)
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(val == None, f"Function {function} should return dictionary, now it returns value which is {taip} type")
    
    def test_3_one_movie(self):
        test_cases = (("The Birds", "Alfred Hitchcock", 1963, 119), ("The Godfather", "Francis Ford Coppola", 1972, 175))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()

                add_movie = load(exercise, function, 'en')

                movielist = []
                
                correct = [{x : y for x,y in zip(("name","director","year","runtime"), test_case)}]
                add_movie(movielist, test_case[0], test_case[1], test_case[2], test_case[3])
                

                self.assertEqual(len(correct), len(movielist), f"After the addition, list should contain {len(correct)} items, but it contains {len(movielist)} items: \n{movielist} when the parameters are \n{test_case}")
                self.assertEqual(correct, movielist, f"The result\n{movielist}\ndoes not match with the model solution\n{correct}\nwhen the parameters are\n{test_case}")

    def test_3_several_movies(self):
        test_cases = (("The Birds", "Alfred Hitchcock", 1963, 119),
                      ("The Godfather", "Francis Ford Coppola", 1972, 175),
                      ("Jaws", "Steven Spielberg", 1975, 124),
                      ("Star Wars", "George Lucas", 1977, 121))
        movielist = []
        correct = []
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                add_movie = load(exercise, function, 'en')

                correct.append({x : y for x,y in zip(("name","director","year","runtime"), test_case)})
                add_movie(movielist, test_case[0], test_case[1], test_case[2], test_case[3])
                
                self.assertEqual(len(correct), len(movielist), f"After the addition, list should contain {len(correct)} items;\n{correct}, but it contains {len(movielist)} items: \n{movielist} when the parameters are \n{test_case}")
                self.assertEqual(correct, movielist, f"The result\n{movielist}\ndoes not match with the model solution\n{correct}\nwhen the parameters are\n{test_case}")
              
if __name__ == '__main__':
    unittest.main()
