import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from inspect import getsource

exercise = 'src.powers_of_two'

@points('3.powers_of_two')
class PowersOfTwoTest(unittest.TestCase):
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
        for number in [3, 4, 5, 11, 16, 24, 35, 43, 57, 101, 1021]:

            with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}")
                
                rows = []
                for i in range(0, number):
                    if 2**i > number: 
                        break

                    rows.append(str(2**i))

                self.assertEqual(len(rows), len(output), f"Your program is expected to print out {len(rows)} rows containing numbers with the input {number}, now program prints out {len(output)} rows:\n{output_all}")

                inpt = str(number)
                for i in range(0, number):
                    if 2**i > number: 
                        break
                    expected = str(2**i)
                    rows_str = '\n'.join(rows)
                    self.assertEqual(expected, output[i], f"Print out in row {i+1} is incorrect when the input is {number}\nyour program is expected to print out:\n{rows_str}\nyour program printed out:\n{output_all}")
    
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")
            if 'break' in line:
                self.assertTrue(False, f"It is not allowed to solve this exercise using while True -command, so your code should not include the following line:\n{line}")

if __name__ == '__main__':
    unittest.main()