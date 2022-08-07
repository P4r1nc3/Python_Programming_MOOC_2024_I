import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout
from functools import reduce
import textwrap

exercise = 'src.word_squared'

@points('3.word_squared')
class WordSquaredTest(unittest.TestCase):
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
        
    def test_function_exists(self):
        try:
            clear_stdout()
            self.module.squared("ab", 2)
        except:
            self.assertTrue(False, f'Your code should contain function named as squared, which can be called as follows:\nsquared("ab", 2)')

    def test_square(self):
        for word, size in [("ab", 3), ("abc", 5), ("python", 15), ('qwerty', 37), ('123456789', 100)]:
            with patch('builtins.input', side_effect=["2"] * 100):
                reload_module(self.module)
                output_at_start = get_stdout()
                clear_stdout()
                try:
                    self.module.squared(word, size)
                except:
                    self.assertTrue(False, f'Make sure that following function call works\nsquared("{word}", {size})')

                output_all = get_stdout().replace(output_at_start, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]
                rows = textwrap.wrap(word*(size*size), size)[0:size]

                self.assertTrue(len(output_all)>0, f'Function call squared("{word}", {size}) does not print out anything')
                acual = '\n'.join(output)
                self.assertEqual(len(rows), len(output), f'Function call squared("{word}", {size}) should print out {size} rows, now it printed out {len(output)} rows, print out was\n{acual}')
                
                for i in range(size):
                    self.assertEqual(rows[i], output[i].strip(), f'Row {i}, which function call squared("{word}", {size}) prints out, should be {rows[i]}, now it is\n{output[i]}\nwhole print out of the function was\n{acual}')

if __name__ == '__main__':
    unittest.main()