import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.sum_of_lists'
function = 'list_sum'

def get_correct(l1: list, l2: list) -> list:
    return [x + y for x,y in zip(l1,l2)]

@points('4.sum_of_lists')
class SumOfListsTest(unittest.TestCase):
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
            from src.sum_of_lists import list_sum
        except:
            self.assertTrue(False, 'Your code should contain function named as list_sum(list1: list, list2: list)')
        try:
            list_sum = load(exercise, function, 'en')
            list_sum([1],[1])
        except:
            self.assertTrue(False, 'Test function call\nlist_sum([1],[1])')


    def test_2_type_of_return_value(self):
        list_sum = load(exercise, function, 'en')
        val = list_sum([1],[2])
        self.assertTrue(type(val) == list, f"Calling {function} does not return list when calling list_sum([1],[2])")

    def test_3_numbers_1(self):
        test_cases = [([1,2,3], [1,2,3]), ([2,4,6], [3,5,7]), ([1,2,1,2,1,2],[2,3,4,5,6,7])]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                list_sum = load(exercise, function, 'en')

                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[:]
                test_result = list_sum(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling list_sum({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

    def test_4_numbers_2(self):
        test_cases = [([10,10,10,11], [99,999,9,99]), ([-10,-11,-12], [1,2,3]), ([100,101,102,103,104],[99,98,97,96,95])]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                list_sum = load(exercise, function, 'en')

                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[:]
                test_result = list_sum(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling list_sum({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {list(test_case2)} but it is {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()
