import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.matrix'

def get_correct() -> dict:
    pass

testdata = ["matrix.txt"]

import os
from shutil import copyfile

@points('6.matrix')
class MatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("input is not required")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be included inside
if __name__ == "__main__":
block. The following code needs to be relocated::
"""
        self.assertTrue(ok, message+line)

    def test_1_functions_exist(self):
            try:
                from src.matrix import row_sums
            except:
                self.assertTrue(False, f'Your code should have a function called row_sums()')  
            try:           
                row_sums()
            except:
                self.assertTrue(False, f'Ensure that call row_sums() can be made!')

            try:
                from src.matrix import matrix_max
            except:
                self.assertTrue(False, f'Your code should have a function called matrix_max')
            try:
                matrix_max()
            except:
                self.assertTrue(False, f'Ensure that call matrix_max() can be made!')

            try:
                from src.matrix import matrix_sum
            except:
                self.assertTrue(False, f'Your code should have a function called matrix_sum')    
            try:
                matrix_sum()
            except:
                self.assertTrue(False, f'Ensure that call matrix_sum() can be made!')     

    def test_2_return_types(self):
       
            funcs = "matrix_sum matrix_max".split()
            for func in funcs:
                    fn = load(exercise, func, 'en')
                    val = fn()
                    taip = str(type(val)).replace("<class '", '').replace("'>","")
                    self.assertTrue(type(val) == int, f"Funtion {func}() should return an integer, now it returns value {val} which is of type {taip}.")
         
            fn = load(exercise, "row_sums", 'en')
            val = fn()
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == list, f"Function row_sums() should return a list, now it returns value {val} which is of type {taip}.")

    def test_3_test_sum(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            matrix_sum = load(exercise, "matrix_sum", 'en')

            val = matrix_sum()
            correct = 4542
            
            self.assertEqual(val, correct, f"Calling matrix_sum() return value {val}, correct answer is {correct}.")

    def test_4_testaa_maksimi(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            matrix_max = load(exercise, "matrix_max", 'en')

            val = matrix_max()
            correct = 965
            
            self.assertEqual(val, correct, f"Calling matrix_max() returns value {val}, correct answer is {correct}.")

    def test_5_testaa_rivisummat(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            row_sums = load(exercise, "row_sums", 'en')

            val = row_sums()
            correct = [-1322, -41, 417, 916, 588, 1031, 880, 1748, -2421, -478, 3776, 346, 309, -881, -326]
            
            self.assertTrue(val == correct, f"Calling row_sums() returns valuen\n{val}\ncorrect answer is\n{correct}")
                    
if __name__ == '__main__':
    unittest.main()
