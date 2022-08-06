import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.countdown'

@points('3.countdown')
class CountdownTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        with patch('builtins.input', side_effect = "2"):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input 2")

    def test_1(self):
        for number in [3, 4, 5, 7, 9, 11, 21, 100]:

            with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}")
                self.assertEqual(number+2, len(output), f"Your program is expected to print out {number+2} rows containing numbers with the input {number}, now program prints out {len(output)} rows:\n{output_all}")

                self.assertEqual("Are you ready?", output[0], f"First row in output is expected to be\nAre you ready?\nnow it is:\nV{output[0]}")
                self.assertEqual("Now!", output[len(output)-1], f"Last row in output is expected to be\nVNow!\nnow it is:{output[len(output)-1]}")

                for i in range(1, number+1):
                    self.assertEqual(str(number-i+1), output[i], f"Print out in row {i+1} is incorrect when input is {number}\nyour program prints out:\n{output_all}")
    
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")
            if 'break' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")

if __name__ == '__main__':
    unittest.main()