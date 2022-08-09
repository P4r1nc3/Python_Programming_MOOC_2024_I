import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.integers_to_strings'
function = 'formatted'

def get_correct(test_case: list) -> list:
    return [f"{x:.2f}" for x in test_case]


@points('4.integers_to_strings')
class IntegersToStringsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_3_numbers1(self):
        for test_case in [[0.123, 1.23, 0.0234], [1.222, 0.33333, 0.6666, 0.9999]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                formatted = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = formatted(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling formatted({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {test_case2} but it is {test_case}.")

    def test_4_numbers2(self):
        for test_case in [[1.00023, 0.987, 0.55543, 1.76], [1.0, 2.33333, 44.11]]:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                formatted = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = formatted(test_case)

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the expected result {correct} when calling formatted({test_case2})")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The list should be {test_case2} but it is {test_case}.")
            
if __name__ == '__main__':
    unittest.main()