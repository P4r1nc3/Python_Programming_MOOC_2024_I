import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.line'

@points('4.line')
class LineTest(unittest.TestCase):
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
            from src.line import line
        except:
            self.assertTrue(False, f'Your code should contain function named as line')
        try:
            from src.line import line
            line(5,"-")
        except:
            self.assertTrue(False, f'Make sure that function can be called as follows:\nvline(5, "-")')

    def test_2_function_can_be_called_with_empty_string(self):
        try:
            from src.line import line
            line(5,"")
        except:
            self.assertTrue(False, f'Calling function as follows should work: line(5, "")')

    def test_3_line_ok_1(self):
        for size, character in [(5, "-"), (12, "-"), (3, "x"), (14, "x"), (19, "%"), (1, "%"), (5, "XXX"),(19, "<3"), (1, "<3"), (5, ":-)")]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_at_start = get_stdout()
            from src.line import line
            line(size, character)
            output_all = get_stdout().replace(output_at_start, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            if len(character)==0:
                character = "*"
            self.assertTrue(len(output_all)>0, f'Calling line({size}, "{character}") does not print out anything')
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f'Calling line({size}, "{character}") should print out only one row, now it prints out {len(output)} rows, the print out was\n{acual}')
            self.assertEqual(character[0]*size, output[0].strip(), f'Calling line({size}, "{character}") should print out row:\n{character[0]*size}\nbut it is:\n{output[0]}')

    def test_4_line_ok_2(self):
        for size, character in [ (3, ""), (5, ""), (12, ""), (14, "")]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_at_start = get_stdout()
            from src.line import line
            line(size, character)
            output_all = get_stdout().replace(output_at_start, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            if len(character)==0:
                character = "*"
            self.assertTrue(len(output_all)>0, f'Calling line({size}, "") does not print out anything')
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f'Calling line({size}, "") should print out only one row, now it prints out {len(output)} rows, the print out was\n{acual}')
            self.assertEqual(character[0]*size, output[0].strip(), f'Calling line({size}, "") should print out row:\n{character[0]*size}\nbut it is:\n{output[0]}')

if __name__ == '__main__':
    unittest.main()