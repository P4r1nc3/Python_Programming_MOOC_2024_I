import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
import os

exercise = 'src.letter_square'

@points('3.letter_square')
class LetterSquareTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_2(self):
        number = 2
        with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output_all =  get_stdout()
            output = output_all.split('\n')  

            expected = [
                "BBB", 
                "BAB", 
                "BBB"
            ]

            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
            """
            #{mssage}") 

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}\n{mssage}") 
            self.assertEqual(len(expected), len(output), f"Your program should print out {len(expected)} rows with the input {number}, now it prints out {len(output)} rows:\n{output_all}")

            for i in range(0, len(expected)):
                self.assertEqual(expected[i], output[i].strip(), f"The print out on {i+1} row is incorrect when the input is {number}, row should be\n{expected[i]}\nThe whole print out was\n{output[0]}")

    def test_3(self):
        number = 3
        with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output_all =  get_stdout()
            output = output_all.split('\n')  

            expected = [
                "CCCCC", 
                "CBBBC", 
                "CBABC",
                "CBBBC",
                "CCCCC"
            ]

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}")
            self.assertEqual(len(expected), len(output), f"Your program should print out {len(expected)} rows with the input {number}, now it prints out {len(output)} rows:\n{output_all}")

            for i in range(0, len(expected)):
                self.assertEqual(expected[i], output[i].strip(), f"The print out on {i+1} row is incorrect when the input is {number}, row should be\n{expected[i]}\nThe whole print out was\n{output[0]}")

        def test_4(self):
            number = 4
            with patch('builtins.input', side_effect=[str(number), AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                expected = [
                    "DDDDDDD"
                    "DCCCCCD", 
                    "DCBBBCD", 
                    "DCBABCD",
                    "DCBBBCD",
                    "DCCCCCD",
                    "DDDDDDD"
                ]

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input {number}")
                self.assertEqual(len(expected), len(output), f"Your program should print out {len(expected)} rows with the input {number}, now it prints out {len(output)} rows:\n{output_all}")

                for i in range(0, len(expected)):
                    self.assertEqual(expected[i], output[i].strip(), f"The print out on {i+1} row is incorrect when the input is {number}, row should be\n{expected[i]}\nThe whole print out was\n{output[0]}")


if __name__ == '__main__':
    unittest.main()