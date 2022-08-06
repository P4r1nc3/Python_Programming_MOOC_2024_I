import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.string_multiplied'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.string_multiplied')
class StringMultipliedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a', '1']):
            cls.module = load_module(exercise, 'en')

    def test_strings(self):
        values = [("hiya","1"),("abc",4),("xyx",7),("hello",2),("test",6)]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works correctly with the input {test_case}")
                out = get_stdout()
                output = out.split("\n")
                corr = test_case[0] * int(test_case[1])
                self.assertTrue(len(out) > 0, "Your program does not print out anything with the inputs {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Instead of printing out only one row in addition to asking for the inputs from the user, your program's print out is now in {len(output)} rows.")
                self.assertEqual(out.strip(), corr, f"The print out is incorrect with the inputs {test_case}: your program's print out is\n{out}\nwhen correct print out is\n{corr}")

if __name__ == '__main__':
    unittest.main()