import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.number_of_elements'
function = 'count_matching_elements'

def get_correct(test_case: list, n: int) -> int:
    return reduce((lambda x,y: x + y), test_case).count(n)


@points('5.count_matching_elements')
class NumberOfElementsTest(unittest.TestCase):
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
            from src.number_of_elements import count_matching_elements
        except:
            self.assertTrue(False, 'Your code should contain function named as count_matching_elements(my_matrix: list, element: int)' )
        try:
            from src.number_of_elements import count_matching_elements
            count_matching_elements([[1, 2]], 1)
        except:
            self.assertTrue(False, 'Make sure, that function can be called as follows\ncount_matching_elements([[1, 2]], 1)' )

    def test_2_type_of_return_value(self):
        count_matching_elements = load(exercise, function, 'en')
        val = count_matching_elements([[1]], 1)
        self.assertTrue(type(val) == int, f"Function {function} does not return value of integer type with parameter values [[1]], 1.")
    
    def test_3_matrices(self):
        test_cases = (([[1,2,3],[2,3,1],[4,5,6]], 2), ([[1,5,5,3],[2,5,2,5],[0,0,2,5]], 5), ([[1,2,3,4],[2,3,4,5],[3,4,6,5]], 6))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                count_matching_elements = load(exercise, function, 'en')
                
                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[0][:]
            
                try:
                    test_result = count_matching_elements(test_case[0], test_case[1])
                except:
                    self.assertTrue(False, f"Make sure that the function works when matrice is {test_case[0]} and element is {test_case[1]}")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when matrice is {test_case[0]} and element is {test_case[1]}")
                self.assertEqual(test_case[0], test_case2, f"Function should not change the original list. The value should should be {test_case2} but it is {test_case}.")

    def test_4_random(self):
        for i in range(5):
            test_case = []
            length = randint(3,6)
            for j in range(randint(3,6)):
                test_case.append([randint(1,5) for i in range(length)])
            
            val = randint(1,5)

            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                count_matching_elements = load(exercise, function, 'en')
                
                correct = get_correct(test_case, val)
                test_case2 = test_case[:]
        
                try:
                    test_result = count_matching_elements(test_case, val)
                except:
                    self.assertTrue(False, f"Make sure that the function works when matrice is {test_case} and element is {val}")


                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when matrice is  {test_case} and element is {val}.")
                self.assertEqual(test_case, test_case2, f"Function should not change the original list. The value should should be {test_case2} but it is {test_case}.")
              
if __name__ == '__main__':
    unittest.main()