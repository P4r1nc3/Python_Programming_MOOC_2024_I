import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from inspect import getsource

exercise = 'src.consecutive_sum_v2'

@points('3.consecutive_sum_v2')
class ConsecutiveSumV2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["3"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        with patch('builtins.input', side_effect = "3"):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input 3")

    def test_1(self):
        for number in [3, 4, 5, 6, 7, 8, 9, 10, 15, 21, 33]:

            with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output =  get_stdout()

                self.assertTrue(len(output)>0, f"Your program does not print out anything with the input {number}")
                rows = len(output.split('\n'))
                self.assertEqual(1, rows, f"Your program should print out only one row, with the input {number} it printed out {rows} rows")

                limit = 1
                sum = 0
                while sum<number:
                    sum += limit
                    limit += 1

                calculation_str = ' + '.join(str(i) for i in range(1, limit) )
    
                expected = 'The consecutive sum: '+calculation_str+" = "+ str(sum)
                self.assertTrue(sanitize(expected) == sanitize(output), f"Your program should print out\n{expected}\nwith the input {number}. Your program printed out\n{output}")

    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")
            if 'break' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")

if __name__ == '__main__':
    unittest.main()