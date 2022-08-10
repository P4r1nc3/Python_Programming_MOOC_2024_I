import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint, shuffle

exercise = 'src.sudoku_add_to_copy'
function1 = 'copy_and_add'

def p(sudoku):
    j = 0
    m = 's = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],\n'
        j += 1
    return m +']' 

@points('5.sudoku_add_to_copy')
class SudokuCopyAndAddTest(unittest.TestCase):
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

    def test_1_function_copy_and_add_exists(self):
        try:
            from src.sudoku_add_to_copy import copy_and_add
        except:
            self.assertTrue(False, f'Your code should contain function named as copy_and_add(sudoku: list, row_no: int, column_no: int, number:int)')
     
        try:
            copy_and_add = load(exercise, function1, 'en')
            s = [
                [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
                [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
                [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
                [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
                [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
                [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
                [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
                [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
                [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
            ]
            copy_and_add(s, 0, 1, 3)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\n{p(s)}\ncopy_and_add(s, 0, 1, 3)')
     
    def test_2_type_of_return_value(self):
          copy_and_add = load(exercise, function1, 'en')
          s = [
              [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
              [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
              [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
              [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
              [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
              [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
              [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
              [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
          ]
          res = copy_and_add(s, 0, 1, 3)
          self.assertFalse(res == None, f'Function copy_and_add should return two-dimensional list of integer values. Now function does not return anything')
          self.assertTrue(type(res) is list, f'Function copy_and_add should return two-dimensional list of integer values. The return value of the function is now\n{res}')
          try:   
            self.assertTrue(type(res[0]) is list, f'Function copy_and_add should return two-dimensional list of integer values. The return value of the function is now\n{res}')
            self.assertTrue(type(res[0][0]) is int, f'Function copy_and_add should return two-dimensional list of integer values. The return value of the function is now\n{res}')
          except:
            self.assertTrue(False, f'Function copy_and_add should return two-dimensional list of integer values. The return value of the function is now\n{res}')
          self.assertTrue(len(res) == len(s), f'When calling\n{p(s)}\copy_and_add(s, 0, 1, 3) the size of the matrix that function returns, should be equal to the parameters size, now it was\n{res}')
          self.assertTrue(len(res[0]) == len(s[0]), f'When calling\n{p(s)}\copy_and_add(s, 0, 1, 3) the size of the matrix that function returns, should be equal to the parameters size, now it was\n{res}')

    def test_3_function_works_1(self):  
        copy_and_add = load(exercise, function1, 'en')
        for r, s, number in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]

          try:
            res = copy_and_add(sudoku, r, s, number)
          except:
             self.assertTrue(False, f"Make sure, that the following function call works\n{p(sudoku)}")

          for rno in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            if rno == r:
              o[s] = number
            self.assertEqual(res[rno], o, f"Calling\n{p(sudoku)}\nres = copy_and_add(s, {r}, {s}, {number})\nshould not change the matrix which is given as parameter to the function, row number {rno} of the sudoku should be:\n{o}:\nbut it is:\n{res[rno]}")
              
          for rno in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            self.assertEqual(sudoku[rno], o, f"The row {rno} in matrix returned after calling\n{p(sudoku)}\nres = copy_and_add(s, {r}, {s}, {number})\n {rno} should still be:\n{o}:\nbut it has been changed to:\n{res[rno]}")

    def test_4_function_works_2(self):  
        copy_and_add = load(exercise, function1, 'en')
        for r, s, number in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]
          original = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]

          for rr in range(9):
            rivi = [1,2,3,4,5,6,7,8,9]
            shuffle(rivi)

            for ss in range(9):
              if randint(1,10)>5 and not (rr!=r and ss!=s):
                number = rivi[ss]
                sudoku[r][s] = number
                original[r][s] = number

          try:
            res = copy_and_add(sudoku, r, s, number)
          except:
             self.assertTrue(False, f"Make sure, that following function call works properly:\n{p(sudoku)}")

          for rno in range(9):
            o = sudoku[rno]
            if rno == r:
              o[s] = number
            self.assertEqual(res[rno], o, f"Calling\n{p(sudoku)}\nres = copy_and_add(s, {r}, {s}, {number})\nshould not change the matrix which is given as parameter to the function, row number {rno} of the sudoku should be:\n{o}:\nbut it is:\n{res[rno]}")
              
          for rno in range(9):
            o = original[rno]
            self.assertEqual(sudoku[rno], o, f"The row {rno} in matrix returned after calling\n{p(sudoku)}\nres = copy_and_add(s, {r}, {s}, {number})\n {rno} should still be:\n{o}:\nbut it has been changed to:\n{res[rno]}")

if __name__ == '__main__':
    unittest.main()
