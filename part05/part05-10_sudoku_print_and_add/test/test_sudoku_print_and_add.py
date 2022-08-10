import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_print_and_add'
function1 = 'add_number'
function2 = 'print_sudoku'

def p(sudoku):
    j = 0
    m = 's = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],\n'
        j += 1
    return m +']' 

@points('5.sudoku_print_and_add')
class SudokuPrintAndAddTest(unittest.TestCase):
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

    def test_1_function_print_sudoku_exists(self):
        try:
            from src.sudoku_print_and_add import print_sudoku
        except:
            self.assertTrue(False, f'Your code should contain function named as print_sudoku(sudoku: list)')
        try:
            from src.sudoku_print_and_add import print_sudoku
            print_sudoku = load(exercise, function2, 'en')
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
            print_sudoku(s)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\n{p(s)}\nprint_sudoku(s)')

    def test_2_printout_is_correct(self):
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
      output_at_start = get_stdout()
      print_sudoku = load(exercise, function2, 'en')
      print_sudoku(s)
      output_all = get_stdout().replace(output_at_start, '', 1)
      output = [l for l in output_all.split("\n") ]

      expected = [
       "9 _ _  _ 8 _  3 _ _",
        "2 _ _  2 5 _  7 _ _",
        "_ 2 _  3 _ _  _ _ 4",
        "",
        "2 9 4  _ _ _  _ _ _",
        "_ _ _  7 3 _  5 6 _",
        "7 _ 5  _ 6 _  4 _ _",
        "",
        "_ _ 7  8 _ 3  9 _ _",
        "_ _ 1  _ _ _  _ _ 3",
        "3 _ _  _ _ _  _ _ 2"
      ]

      for i in range(len(expected)):
        o = expected[i]
        v = output[i].replace('\n', '').rstrip()
        self.assertEqual(o, v, f'When calling\n{p(s)}\nprint_sudoku(s)\nrow {i+1} in printout is incorrect. The row was:\n{v}\nbut it should be:\n{o}')

    def test_3_printout_is_correct(self):
      s = [
          [2, 6, 7, 8, 3, 9, 5, 0, 4],
          [9, 0, 3, 5, 1, 0, 6, 0, 0],
          [0, 5, 1, 6, 0, 0, 8, 3, 9],
          [5, 1, 9, 0, 4, 6, 3, 2, 8],
          [8, 0, 2, 1, 0, 5, 7, 0, 6],
          [6, 7, 4, 3, 2, 0, 0, 0, 5],
          [0, 0, 0, 4, 5, 7, 2, 6, 3],
          [3, 2, 0, 0, 8, 0, 0, 5, 7],
          [7, 4, 5, 0, 0, 3, 9, 0, 1],
      ]  
      output_at_start = get_stdout()
      print_sudoku = load(exercise, function2, 'en')
      print_sudoku(s)
      output_all = get_stdout().replace(output_at_start, '', 1)
      output = [l for l in output_all.split("\n") ]

      expected = [
        "2 6 7  8 3 9  5 _ 4",
        "9 _ 3  5 1 _  6 _ _",
        "_ 5 1  6 _ _  8 3 9",
        "",
        "5 1 9  _ 4 6  3 2 8",
        "8 _ 2  1 _ 5  7 _ 6",
        "6 7 4  3 2 _  _ _ 5",
        "",
        "_ _ _  4 5 7  2 6 3",
        "3 2 _  _ 8 _  _ 5 7",
        "7 4 5  _ _ 3  9 _ 1"
      ]

      for i in range(len(expected)):
        o = expected[i]
        v = output[i].replace('\n', '').rstrip()
        self.assertEqual(o, v, f'When calling\n{p(s)}\nprint_sudoku(s)\nrow {i+1} in printout is incorrect. The row was:\n{v}\nbut it should be:\n{o}')

    def test_4_function_add_number_exists(self):
        try:
            from src.sudoku_print_and_add import add_number
        except:
            self.assertTrue(False, f'Your code should contain function named as add_number(sudoku: list, row_no: int, column_no: int, number: int)')
        try:
            add_number = load(exercise, function1, 'en')
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
            add_number(s, 0, 1, 3)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\n{p(s)}\nadd_number(s, 0, 1, 3)')

    def test_5_add_number_works(self):
        add_number = load(exercise, function1, 'en')
        for r, s, number in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku  = [
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
            add_number(sudoku, r, s, number)
          except:
             self.assertTrue(False, f"Make sure that following function call works\n{p(sudoku)}\nadd_number(s, {r}, {s}, {number})")

          for rnro in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            if rnro == r:
              o[s] = number
            self.assertEqual(sudoku[rnro], o, f"After executing function call\n{p(sudoku)}\nadd_number(s, {r}, {s}, {number})\nrow {rnro} (counting starts from 0) should be:\n{o}:\nbut it is:\n{sudoku[rnro]}")

if __name__ == '__main__':
    unittest.main()
