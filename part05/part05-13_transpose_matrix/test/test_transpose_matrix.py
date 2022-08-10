import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.transpose_matrix'
function = 'transpose'

def get_correct(test_case: list) -> int:
    pass

@points('5.transpose_matrix')
class MatrixTest(unittest.TestCase):
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
            from src.transpose_matrix import transpose
        except:
            self.assertTrue(False, 'Your code should contain function named as transpose(matrix: list)')

        try:
            transpose = load(exercise, function, 'en')
            transpose([[1,2],[1,2]])
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows:\ntranspose([[1,2],[1,2]])')

    def test_2_type_of_return_value(self):
        transpose = load(exercise, function, 'en')
        val = transpose([[1,2],[1,2]])
        self.assertTrue(val == None, f"Function {function} should not return a value.")

    def test_3_matrices_1(self):
        test_cases = (([[1,2],[1,2]], [[1,1],[2,2]]), ([[0,1,2],[0,1,2],[0,1,2]], [[0,0,0],[1,1,1],[2,2,2]]))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                transpose = load(exercise, function, 'en')

                test_matrix = test_case[0]
                test_matrix2 = [r[:] for r in test_case[0]]
                try:
                    transpose(test_matrix)
                except:
                    self.assertTrue(False, f"Make sure, that the function works when the input is \n{test_matrix2}")

                correct = test_case[1]

                self.assertEqual(test_matrix, correct, f"The result \n{test_matrix} does not match with the model solution \n{correct} when the parameter is \n{test_matrix2}")

    def test_4_matrices_2(self):
        test_cases = (([[10,100],[10,100]], [[10,10],[100,100]]), ([[2,3,4,5],[6,7,8,9],[9,8,7,6],[5,4,3,2]], [[2,6,9,5],[3,7,8,4],[4,8,7,3],[5,9,6,2]]))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                transpose = load(exercise, function, 'en')

                test_matrix = test_case[0]
                test_matrix2 = [r[:] for r in test_case[0]]
                try:
                    transpose(test_matrix)
                except:
                    self.assertTrue(False, f"Make sure, that the function works when the input is \n{test_matrix2}")

                correct = test_case[1]

                self.assertEqual(test_matrix, correct, f"The result \n{test_matrix} does not match with the model solution \n{correct} when the parameter is \n{test_matrix2}")
       
if __name__ == '__main__':
    unittest.main()