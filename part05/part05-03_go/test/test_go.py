import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.go'
function = 'who_won'

def get_correct(test_case: list) -> int:
    c = [(reduce((lambda x,y: x + y), test_case).count(n), n) for n in (1,2)]
    return max(c)[1] if c[0][0] != c[1][0] else 0


@points('5.go')
class GoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message =  """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.go import who_won
        except:
            self.assertTrue(False, 'Your code should contain function named as who_won(game_board: list)')
        try:
            who_won = load(exercise, function, 'en')
            who_won([[1]])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\nwho_won([[1]])')

    def test_2_type_of_return_value(self):
        who_won = load(exercise, function, 'en')
        val = who_won([[1]])
        self.assertTrue(type(val) == int, f"Function {function} does not return value of string type with the parameter values [[1]], 1.")
    
    def test_3_ready_made_boards(self):
        test_cases = (([[1,2,1],[0,0,1],[2,1,0]], 1), ([[1,2,2,2],[0,0,0,1],[0,0,2,1]], 2), ([[1,2,2,2],[2,1,1,1],[0,2,1,0]], 0))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                who_won = load(exercise, function, 'en')
                
                correct = test_case[1]
                test_case2 = test_case[0][:]
                try:
                    test_result = who_won(test_case[0])
                except:
                    self.assertTrue(False, f"Make sure that the function works when the matrice is {test_case[0]}")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when the matrice is {test_case[0]}")
                self.assertEqual(test_case[0], test_case2, f"Function should not change the original list. The value should should be {test_case2} but it is {test_case[0]}.")

    def test_4_random_boards(self):
        for i in range(5):
            test_case = []
            length = randint(5,10)
            for j in range(length):
                test_case.append([randint(0,2) for x in range(length)])
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                who_won = load(exercise, function, 'en')
                
                correct = get_correct(test_case)
                test_case2 = test_case
                try:
                    test_result = who_won(test_case)
                except:
                    self.assertTrue(False, f"Make sure that the function works when the matrice is {test_case}")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when the matrice is \n{test_case}")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {test_case2} but it is {test_case}.")
       
if __name__ == '__main__':
    unittest.main()