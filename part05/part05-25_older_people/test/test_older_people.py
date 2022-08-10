import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.older_people'
function = 'older_people'


@points('5.older_people')
class OlderPeopleTest(unittest.TestCase):
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
            from src.older_people import older_people
        except:
            self.assertTrue(False, f'Your code should contain function named as older_people(people: list, year: int)')
        try:
            older_people = load(exercise, function, 'en')
            code = """person_list = [("Arthur", 1977), ("Emily", 2014)]
older_people(person_list, 2000)"""

            person_list = [("Arthur", 1977), ("Emily", 2014)]
            older_people(person_list, 2000)

        except:
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code:\n{code}')

    def test_2_type_of_return_value(self):
        older_people = load(exercise, function, 'en')
        code = """person_list = [("Arthur", 1977), ("Emily", 2014)]
result = older_people(person_list, 2000)"""

        person_list = [("Arthur", 1977), ("Emily", 2014)]
        result = older_people(person_list, 2000)

        self.assertTrue(type(result) == list, f"Function {function} does not return a list when executing the following code:\n{code}")

    def test_3_functionality(self):
        older_people = load(exercise, function, 'en')
        for person_list in [ 
                [("Arthur", 1977), ("Emily", 2014)],
                [("Emily", 2014), ("Arthur", 1977)],
                [("Emily", 2014), ("Arthur", 1977), ("Ernest", 1985),  ("Mary", 1953), ("Ellen", 1997)],
                [("Jacob", 2016), ("Harry", 2019), ("Oliver", 2012),  ("Wendy", 2013), ("Jane Doe", 2020)],
                [("Donald", 1982), ("Daisy", 1892), ("Angela", 1965),  ("Vladimir", 2000), ("Dunja", 1919), ("Elizabeth", 1921)]
            ]:

            for year in [2010, 2000, 1990, 1980, 1970, 1950, 1900]:

                code = f"person_list = {person_list}\n"+f"result = older_people(person_list, {year})"
                result = older_people(person_list, year)
                correct = [ n for n, i in person_list if i < year]

                self.assertEqual(result, correct, f"The result {result} returned by function {function} is incorrect, function should return {correct} when executing the following code\n{code}")

if __name__ == '__main__':
    unittest.main()
