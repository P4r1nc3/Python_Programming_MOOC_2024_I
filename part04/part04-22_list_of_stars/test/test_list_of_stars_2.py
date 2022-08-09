import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.list_of_stars'
function = 'list_of_stars'

def get_correct(lst: list) -> str:
    return "\n".join(["*" * x for x in lst])

@points('4.list_of_stars')
class ListOfStarsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_4_numbers_1(self):
        test_cases = ([2,2],[1,1,1,1],[1,2,3,2,1],[5,4,3,2,1],[2,2,2],[8,6,2,4,6])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                from src.list_of_stars import list_of_stars
                list_of_stars(test_case)
                
                correct = get_correct(test_case)

                output_alussa = get_stdout()
                list_of_stars(test_case)
                output = get_stdout().replace(output_alussa+'\n', '', 1)
                self.assertEqual(len(correct), len(output), f"The amount of the rows printed out is incorrect with the test input {test_case}. Your function printed out {len(output)} rows, correct amount is {len(correct)}")
                self.assertEqual(correct, output, f"The result:\n{output}\ndoes not match with the model solution\n{correct}\nwith the test input {test_case}.")

    def test_5_numbers_2(self):
        test_cases = ([9,9,9,9],[1,0,1,0,1],[5,5,3,3,1,1,3,3,5,5])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                from src.list_of_stars import list_of_stars
                list_of_stars(test_case)

                correct = get_correct(test_case)

                output_at_start = get_stdout()
                list_of_stars(test_case)
                output = get_stdout().replace(output_at_start+'\n', '', 1)

                self.assertEqual(correct, output, f"The result:\n{output}\ndoes not match with the model solution\n{correct}\nwith the test input {test_case}.")
        
if __name__ == '__main__':
    unittest.main()