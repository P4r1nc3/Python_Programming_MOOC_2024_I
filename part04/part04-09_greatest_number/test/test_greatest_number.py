import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.greatest_number'

@points('4.greatest_number')
class GreatestNumberTest(unittest.TestCase):
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
            from src.greatest_number import greatest_number
        except:
            self.assertTrue(False, f'Your code should contain function named as greatest_number')
        try:
            from src.greatest_number import greatest_number
            greatest_number(5, 3, 7)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows:\ngreatest_number(3, 5, 7)')

    def test_2_function_ok(self):
        for a, b, c in [(3,5,7), (9, -1, 3), (1,1,1), (4,5,5), (-1, 9, 3), (12,11, 10), (-100, 100, -200), (2,1,2), (1,1,-100), (7, 3, 5), (5,7,3), (42, 42, 42), (1, 0, -1) ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.greatest_number import greatest_number
                ret = greatest_number(a,b,c)
                output_all = get_stdout().replace(output_at_start, '', 1)

                self.assertFalse(ret == None, f'Calling greatest_number({a}, {b}, {c}) should return {max([a, b, c])} now it does not return anything. Make sure that you use return command in your function')
                self.assertEqual(ret, max([a, b, c]), f'Calling greatest_number({a}, {b}, {c}) should return {max([a, b, c])} now it returns {ret}')
                self.assertFalse(len(output_all)>0, f'Calling greatest_number({a}, {b}, {c}) should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

if __name__ == '__main__':
    unittest.main()
