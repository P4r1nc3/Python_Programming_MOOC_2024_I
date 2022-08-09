import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.length_of_list'

def f(list):
    return '[' +', '.join([str(i) for i in list]) +']' 

@points('4.length_of_list')
class LengthOfListTest(unittest.TestCase):
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
            from src.length_of_list import length
        except:
            self.assertTrue(False, f'Your code should contain function named as length(items: list)')
        try:
            from src.length_of_list import length
            list = [1, 2, 3]
            length(list)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows length([1, 2, 3])')

    def test_2_functionality_ok(self):
        for list in [[1,2,3], [1,3,67,7,4,23,1,5,7,4], [1], [], [33,4,4,5,7,43,32,1,3,6,7,7,4], [1,1,1,1,1,1,1], [0,0,1,2,3,4,5,6,7,8]]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.length_of_list import length
                res = length(list)
                output_all = get_stdout().replace(output_at_start, '', 1)
                expected = len(list)

                self.assertFalse(res == None, f'Calling length({f(list)}) should return {expected} now it does not return anything. Make sure that you use return command in any cases in your function!')
                self.assertEqual(res, expected, f'Calling length({f(list)}) should return {expected} now it returns {res}')
                self.assertFalse(len(output_all)>0, f'Calling length({f(list)}) should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

if __name__ == '__main__':
    unittest.main()