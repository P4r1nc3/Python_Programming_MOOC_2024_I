import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.oldest_person'
function = 'oldest_person'


@points('5.oldest_person')
class OldestPersonTest(unittest.TestCase):
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
            from src.oldest_person import oldest_person
        except:
            self.assertTrue(False, f'Your code should contain function named as oldest_person(people: list)')
        try:
            oldest_person = load(exercise, function, 'en')
            code = """people_list = [("Arthur", 1977), ("Emily", 2014)]
oldest_person(people_list)"""

            people_list = [("Arthur", 1977), ("Emily", 2014)]
            oldest_person(people_list)

        except:
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code:\n{code}')


    def test_2_type_of_return_value(self):
        oldest_person = load(exercise, function, 'en')
        code = """people_list = [("Arthur", 1977), ("Emily", 2014)]
result = oldest_person(people_list)"""

        people_list = [("Arthur", 1977), ("Emily", 2014)]
        result = oldest_person(people_list)

        self.assertTrue(type(result) == str, f"Function {function} does not return string value when executing the following code:\n{code}")

    def test_3_functionality(self):
        oldest_person = load(exercise, function, 'en')
        for people_list in [ 
                [("Arthur", 1977), ("Emily", 2014)],
                [("Emily", 2014), ("Arthur", 1977)],
                [("Emily", 2014), ("Arthur", 1977), ("Ernest", 1985),  ("Mary", 1953), ("Ellen", 1997)],
                [("Jacob", 2016), ("Harry", 2019), ("Oliver", 2012),  ("Wendy", 2013), ("Jane Doe", 2020)],
                [("Donald", 1982), ("Daisy", 1892), ("Angela", 1965),  ("Vladimir", 2000), ("Dunja", 1919), ("Elizabeth", 1921)]
            ]:
            code = f"people_list = {people_list}\n"+"result = oldest_person(people_list)"
            result = oldest_person(people_list)
            correct = [ n for n, i in people_list if i == min( i for n, i in people_list)][0]

            self.assertEqual(result, correct, f"The result {result} returned by function {function} is incorrect, function should return {correct} when executing the following code\n{code}")

if __name__ == '__main__':
    unittest.main()
