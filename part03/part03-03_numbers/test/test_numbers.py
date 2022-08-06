import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.numbers'

@points('3.numbers')
class NumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        with patch('builtins.input', side_effect = "2"):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input 2")

    def test_1(self):
        for number in [3, 5, 7, 10, 13, 17, 21, 1001]:

            with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}")
                self.assertEqual(number-1, len(output), f"Your program is expected to print out {number-1} rows containing numbers with the input {number}, now program prints out {len(output)} rows:\n{output_all}")

                inpt = str(number)
                for i in range(1, number):
                    expected = str(i)
                    self.assertEqual(str(i), output[i-1], f"Print out in row {i} is incorrect when the input is {number}")
    
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")
            if 'break' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")

if __name__ == '__main__':
    unittest.main()