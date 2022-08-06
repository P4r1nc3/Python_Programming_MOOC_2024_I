import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.powers_of_base_n'

@points('3.powers_of_base_n')
class PowersOfBaseNTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["3"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        with patch('builtins.input', side_effect = ["3", "3"]):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input 3 3")

    def test_1(self):
        for limit, multiplier in [(10, 3), (27, 3),(64, 4) ,(47, 3), (30, 5), (150, 7),  (200, 7),  (1000, 11),  (2000, 21)]:
            with patch('builtins.input', side_effect=[str(limit), str(multiplier), AssertionError("Input is asked too many times.") ] ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {limit}")
                
                rows = []
                for i in range(0, limit):
                    if multiplier**i > limit:
                        break

                    rows.append(str(multiplier**i))

                rows_str = '\n'.join(rows)
                self.assertEqual(len(rows), len(output), f"Your program should print out {len(rows)} rows containing numbers with the input {limit} {multiplier}, now program prints out {len(output)} rows:\n{output_all}\nexpected print out is\n{rows_str}")

                inpt = str(limit)
                for i in range(0, limit):
                    if multiplier**i > limit:
                        break
                    expected = str(multiplier**i)
                    rows_str = '\n'.join(rows)
                    self.assertEqual(expected, output[i], f"Print out in row {i+1} is incorrect when the input is {limit} {multiplier}\nyour program should print out:\n{rows_str}\nyour program printed out:\n{output_all}")

    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")
            if 'break' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")

if __name__ == '__main__':
    unittest.main()
