import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.length_of_longest'
function = 'length_of_longest'

def get_correct(test_case: list) -> list:
    pass

@points('4.length_of_longest')
class LengthOgLongestTest(unittest.TestCase):
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
            from src.length_of_longest import length_of_longest
        except:
            self.assertTrue(False, 'Your code should contain function named as length_of_longest(my_list: list)')
        try:
            length_of_longest = load(exercise, function, 'en')
            length_of_longest(["abc", "ab"])
        except:
            self.assertTrue(False, 'Test function call\nlength_of_longest(["abc", "ab"])')


    def test_2_type_of_return_value(self):
        length_of_longest = load(exercise, function, 'en')
        val = length_of_longest(["Ada", "Kathleen"])
        self.assertTrue(type(val) == int, "Function length_of_longest does not return value of integer type with parameter value ['Ada', 'Kathleen'].")
    
    def test_3_one_is_longest(self):
        test_cases = {("Alan", "Grace", "Frances", "Kim", "Susan") : ["Frances"], 
                      ("Mark", "Paul", "Magdalena", "Jean", "Linus") : ["Magdalena"],
                      ("Seraenina", "Gandalf", "Harry", "Walter") : ["Seraenina"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                length_of_longest = load(exercise, function, 'en')
                
                correct = len(test_cases[test_case][0])
                test_case2 = test_case[:]
                test_result = length_of_longest(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling length_of_longest({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

    def test_4_several_longest(self):
        test_cases = {("Alan", "Grace", "Steve", "Kim", "Susan") : ["Grace", "Steve", "Susan"], 
                      ("Mark", "Paul", "Bill", "Jan", "Tim", "Jean") : ["Mark", "Paul", "Bill", "Jean"],
                      ("Huey", "Dewey", "Louie", "April", "May", "June", "David") : ["Dewey", "Louie", "April", "David"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                length_of_longest = load(exercise, function, 'en')
                
                correct = len(test_cases[test_case][0])
                test_case2 = test_case[:]
                test_result = length_of_longest(list(test_case))

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling length_of_longest({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")
          
if __name__ == '__main__':
    unittest.main()
