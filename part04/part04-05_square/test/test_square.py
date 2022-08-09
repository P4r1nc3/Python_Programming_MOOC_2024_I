import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.square'

def cor_shape(y_height, y_character):
    i = 1
    lines = []
    while i<=y_height:
        lines.append(y_character*y_height)
        i += 1

    return lines

@points('4.square')
class SquareTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
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
            from src.square import square
        except:
            self.assertTrue(False, f'Your code should contain function named as square')
        try:
            from src.square import square
            square(5, "-")
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows:\rsquare(5, "-")')

    def test_2_square_ok(self):
        for y_height, y_character in [(5, "+"),(3, "X"), (4, "x"), (4, "x"),(5, "o"), (1, "^"), (3, "z") ,(20, "@") ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.square import square
                square(y_height, y_character)
                output_all = get_stdout().replace(output_at_start, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

                exp = cor_shape(y_height, y_character)

                self.assertTrue(len(output_all)>0, f'Calling square({y_height}, "{y_character}") does not print out anything')
                acual = '\n'.join(output)
                self.assertEqual(len(exp), len(output), f'Calling square({y_height}, "{y_character}") should print out {len(exp)} rows, now it prints out {len(output)} rows, the print out was\n{acual}')
                for i in range(len(exp)):
                    self.assertEqual(exp[i], output[i].strip(), f'The row {i+1} printed out after calling square({y_height}, "{y_character}") should be:\n{exp[i]}\nbut it is:\n{output[i]}\nWhole print out of the function was\n{output_all}')

    def test_function_line_in_use(self):
        src_file = os.path.join('src', 'square.py')
        with open(src_file) as f:
            in_function = False
            for line in f:
                if 'def square' in line:
                    in_function = True
                elif 'def line' in line:
                    in_function = False
                elif line[0] != " " and line[0] != "#":
                    in_function = False

                if in_function:
                    if '  print' in line:
                        self.assertTrue(False, f"Function square should not use print commands for printing, so following row is not allowed in your code\n{line}")

if __name__ == '__main__':
    unittest.main()