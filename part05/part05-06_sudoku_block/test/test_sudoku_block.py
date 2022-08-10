import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_block'
function = 'block_correct'

def p(sudoku):
    j = 0
    m = '# column numbers\n#   0  1  2  3  4  5  6  7  8\nsudoku = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],   # row {j}\n'
        j += 1
    return m +']' 

@points('5.sudoku_block')
class SudokuBlockTest(unittest.TestCase):
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
            from src.sudoku_block import block_correct

        except:
            self.assertTrue(False, f'Your code should contain function named as block_correct(sudoku: list, row_no: int, column_no: int)')
        try:
            column_correct = load(exercise, function, 'en')
            s = sudoku = [
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
            column_correct(s, 0, 0)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\n{p(s)}\nblock_correct(sudoku, 0, 0)')


    def test_2_type_of_return_value(self):
        block_correct = load(exercise, function, 'en')
        s = sudoku = [
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
        val = block_correct(s, 0, 0)
        self.assertTrue(type(val) == bool, f"Function {function} does not return boolean value when calling\n{p(s)}\nblock_correct(sudoku, 0, 0)")

    def test_3_functionality(self):
        block_correct = load(exercise, function, 'en')
        s = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
            [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ]
        ]

        for row, column in [(0, 3), (0,6), (3,0), (3,3), (6,6)]:
            val = block_correct(s, row, column)
            self.assertEqual(val, True, f"The result {val} is incorrect when calling \n{p(s)}\nblock_correct(sudoku, {row}, {column})")

        for row, column in [(0, 0), (3, 6), (6, 3), (6, 0)]:
            try:
                val = block_correct(s, row, column)
            except: 
                self.assertEqual(val, False, f"Make sure, that the function can be called as follows\n{p(s)}\nblock_correct(sudoku, {row}, {column})")
            self.assertEqual(val, False, f"The result {val} is incorrect when calling \n{p(s)}\nblock_correct(sudoku, {row}, {column})")

if __name__ == '__main__':
    unittest.main()