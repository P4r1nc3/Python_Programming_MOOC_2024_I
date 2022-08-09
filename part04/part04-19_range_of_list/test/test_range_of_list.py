import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.range_of_list'

def f(list):
    return '['+', '.join([str(i) for i in list])+']'

@points('4.range_of_list')
class RangeOfListTest(unittest.TestCase):
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
            from src.range_of_list import range_of_list
            list = [1, 2, 3]
            range_of_list(list)
        except:
            self.assertTrue(False, f'Your code should contain function named as range_of_list(list: list)')
        try:
            from src.range_of_list import range_of_list
            list = [1, 2, 3]
            range_of_list(list)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\nrange_of_list([1, 2, 3])')

    def test_2_functionality_ok(self):
        for list in [[1,2,3], [1,3,67,7,4,23,1,5,7,4], [1], [33,4,4,5,7,43,32,1,3,6,7,7,4], [1,1,1,1,1,1,1], [0,0,1,2,3,4,5,6,7,8], [-100, 10000, 2012, 123, -123, 3123, 323], [-123,123,43,2345,54564,1234,52,6242] ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.range_of_list import range_of_list
                res = range_of_list(list)
                output_all = get_stdout().replace(output_at_start, '', 1)
                expected = max(list)-min(list)

                self.assertFalse(res == None, f'Calling range_of_list({f(list)}) should return {expected} now it does not return anything. Make sure that you use return command in any cases in your function!')
                self.assertEqual(res, expected, f'Calling range_of_list({f(list)}) should return {expected} now it returns {res}')
                self.assertFalse(len(output_all)>0, f'Calling range_of_list({f(list)}) should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

if __name__ == '__main__':
    unittest.main()