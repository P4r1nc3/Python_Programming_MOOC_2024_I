import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.histogram'
function = 'histogram'

@points('5.histogram')
class HistogramTest(unittest.TestCase):
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
            from src.histogram import histogram
        except:
            self.assertTrue(False, f'Your code should contain function named as histogram(my_str: str)')
    
        try:
            histogram = load(exercise, function, 'en')
            koodi = """histogram("abba")"""
            histogram("abba")
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows:\n{koodi}')


    def test_2_abba_works(self):
        histogram = load(exercise, function, 'en')
        
        word = "abba"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            code = F'histogram("{word}")'

            output_at_start = get_stdout()

            histogram(word)

            output_all = get_stdout().replace(output_at_start, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Calling {code} does not print out anything')
            exp = ["a **", "b **"]
            self.assertEqual(len(exp), len(output),  f'Calling {code} should print out {len(exp)} row,but it printed out {len(output)} rows. The print out was\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Calling {code} should print out row \n{rivi}\nbut that row was not found. The print out was\n{output_all}')          

    def test_3_soapbar_works(self):
        histogram = load(exercise, function, 'en')
        
        sana = "soapbar"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            code = F'histogram("{sana}")'

            output_at_start = get_stdout()

            histogram(sana)

            output_all = get_stdout().replace(output_at_start, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Calling {code} does not print out anything')
            exp = [ "s *", "o *", "a **", "p *", "b *", "r *" ]
            self.assertEqual(len(exp), len(output),  f'Calling {code} should print out {len(exp)} row,but it printed out {len(output)} rows. The print out was\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Calling {code} should print out row \n{rivi}\nbut that row was not found. The print out was\n{output_all}')          

    def test_3_histogram_works(self):
        histogram = load(exercise, function, 'en')
        
        word = "histogram"
        with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            code = F'histogram("{word}")'

            output_at_start = get_stdout()

            histogram(word)

            output_all = get_stdout().replace(output_at_start, '', 1)

            output = [l for l in output_all.split("\n") if len(l)>0 ]

            self.assertTrue(len(output_all)>0, f'Calling {code} does not print out anything')
            exp = """h *
i *
s *
t *
o *
g *
r *
a *
m *""".split('\n')
            self.assertEqual(len(exp), len(output),  f'Calling {code} should print out {len(exp)} row,but it printed out {len(output)} rows. The print out was\n{output_all}')
            for rivi in exp:
                self.assertTrue(rivi in output, f'Calling {code} should print out row \n{rivi}\nbut that row was not found. The print out was\n{output_all}')          


if __name__ == '__main__':
    unittest.main()