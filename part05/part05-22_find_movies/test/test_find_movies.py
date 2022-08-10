import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.find_movies'
function = 'find_movies'

def get_correct(l: list, s: str) -> list:
    return [x for x in l if s.lower() in x["name"].lower()]

@points('5.find_movies')
class FindMoviesTest(unittest.TestCase):
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

    def test_1_funktio_olemassa(self):
        try:
            from src.find_movies import find_movies
        except:
            self.assertTrue(False, 'Your code should contain function named as find_movies(database: list, search_term: str)')
        try:
            find_movies = load(exercise, function, 'en')
            find_movies([{"name":"aa", "director":"", "year":1, "runtime":1}], "a")
        except:
            self.assertTrue(False, 'Make sure that function can be called as follows:\nfind_movies([{"name":"aa", "director":"", "year":1, "runtime":1}], "a")')

    def test_2_type_of_return_value(self):
        find_movies = load(exercise, function, 'en')
        val = find_movies([{"name":"aa", "director":"", "year":1, "runtime":1}], "a")
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == list, f"Function {function} should return list, now it returns value {val} which is {taip} type")
    
    def test_3_movies_1(self):
        test_cases = (("The Birds", "Alfred Hitchcock", 1963, 119),
                      ("The Godfather", "Francis Ford Coppola", 1972, 175),
                      ("Jaws", "Steven Spielberg", 1975, 124),
                      ("Star Wars", "George Lucas", 1977, 121))
        movielist = []
        for tc in test_cases:
            movielist.append({x : y for x,y in zip(("name","director","year","runtime"), tc)})
        
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            reload_module(self.module)
            output_at_start = get_stdout()
            find_movies = load(exercise, function, 'en')
            
            correct = get_correct(movielist, "ja")
            answer = find_movies(movielist, "ja")
            
            self.assertEqual(len(correct), len(answer), f"The result should contain {len(correct)} items;\n{correct}, but it contains {len(answer)} items: \n{answer}\nwhen the database contains the following movies \n{movielist} and the search term is 'ja'")
            self.assertEqual(correct, answer, f"The result \n{answer}\ndoes not match with the model solution \n{correct}\nwhen the database contains the following movies \n{movielist}\nand search term is 'ja'")
    
    def test_4_movies_2(self):
        test_cases = (("The Birds 4", "James Hitchcock", 2003, 119),
                      ("The Godfather 4", "Antero Coppola", 2022, 83),
                      ("Jaws", "Steven Spielberg", 1975, 124),
                      ("Star Wars", "George Lucas", 1977, 121),
                      ("Lost in Translation 4", "Soena Coppola", 2032, 120))
        movielist = []
        for tc in test_cases:
            movielist.append({x : y for x,y in zip(("name","director","year","runtime"), tc)})
        
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            reload_module(self.module)
            output_at_start = get_stdout()
            find_movies = load(exercise, function, 'en')
            
            correct = get_correct(movielist, "4")
            answer = find_movies(movielist, "4")
            
            self.assertEqual(len(correct), len(answer), f"The result should contain {len(correct)} items;\n{correct}, but it contains {len(answer)} items: \n{answer} when the database contains the following movies \n{movielist} and the search term is '4'")
            self.assertEqual(correct, answer, f"The result \n{answer}\ndoes not match with the model solution \n{correct}\nwhen the database contains the following movies \n{movielist}\nand the search term is '4'")
    
              
if __name__ == '__main__':
    unittest.main()
