import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.shortest_in_list'
function = 'shortest'

def get_correct(test_case: list) -> list:
    pass

@points('4.shortest_in_list')
class ShortestInListTest(unittest.TestCase):
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
            from src.shortest_in_list import shortest
        except:
            self.assertTrue(False, 'Your code should contain function named as shortest(my_list: list)')
        try:
            shortest = load(exercise, function, 'en')
            shortest(["abc", "ab"])
        except:
            self.assertTrue(False, 'Test function call\nshortest(["abc", "ab"])')

    def test_2_type_of_return_value(self):
        shortest = load(exercise, function, 'en')
        val = shortest(["Alan", "Steve"])
        self.assertTrue(type(val) == str, "Function shortest does not return value of string type with parameter value ['Alan', 'Steve'].")
    
    def test_3_shortest_is_found(self):
        test_cases = {("Alan", "Susan", "Seymour", "Kim", "Susan") : ["Kim"], 
                      ("Mark", "Hedy", "Magdalena", "Mia", "Paul", "David") : ["Mia"],
                      ("Seraenina", "Gandalf", "Harry", "Walter") : ["Harry"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                shortest = load(exercise, function, 'en')
                
                correct = test_cases[test_case][0]
                test_case2 = test_case[:]
                test_result = shortest(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling shortest{test_case2}")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()