import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.same_characters'

@points('4.same_characters')
class SameCharactersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_5_function_ok(self):
        for mj, a, b in [("coder",1,2), ("coder",1,3), ("coder",1,10), ("programming",6,0),  ("programming",10,0),  ("programming",1,2), ("aaaa", 1, 2),  ("abracadabra", 0, 3), ("abracadabra", 0, 4), ("simsalabim", 1, 8),  ("simsalabim", 4, 5),  ("abc", 0, 3), ("simsalabim", 4, 6)]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.same_characters import same_chars
                try:
                    ret = same_chars(mj, a,b)
                except:
                    self.assertTrue(False, f'Make sure that calling function same_chars("{mj}", {a}, {b}) works')

                output_all = get_stdout().replace(output_at_start, '', 1)
                expected = -1 < a < len(mj) and -1 < b < len(mj) and mj[a] == mj[b]

                self.assertFalse(ret == None, f'Calling same_chars("{mj}", {a}, {b}) should return {expected} now it does not return anything. Make sure that you use return command in all cases in your function!')           
                self.assertEqual(ret, expected, f'Calling same_chars("{mj}", {a}, {b}) should return {expected} now it returns {ret}')
                self.assertFalse(len(output_all)>0, f'Calling same_chars("{mj}", {a}, {b}) should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

if __name__ == '__main__':
    unittest.main()