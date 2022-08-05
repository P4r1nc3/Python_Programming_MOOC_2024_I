import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.working_with_numbers'

def pp(a):
    return "\n".join(a)

testset = [
    [str(i) for i in [1, 2, 3, 0, 3, 6, 2.0, 3, 0]],
    [str(i) for i in [5, 0, 1, 5, 5.0, 1, 0]],
    [str(i) for i in [5, 45, -3, 65, 3, 34, -9, 0,  7, 140, 20.0, 5, 2]],
    [str(i) for i in [3, -76, -7, 4, 55, 0, 5, -21, -4.2, 3, 2]]
]

class WorkingWithNumbersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["0"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0(self):
        values = "1 0".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input\n{}".format(pp(values)))

    @points('2.working_with_numbers-part1')
    def test_1_start(self):
        with patch('builtins.input', side_effect=['1', '2', '3', '0', AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()

            inpt = '\n'.join(['1', '2', '3', '0'])

            self.assertFalse(len(output)==0, f"Your program did not print out anything with the input\n{inpt}" )
            expected = "Please type in integer numbers. Type in 0 to finish."
            self.assertEqual(expected, output.split('\n')[0].strip(), f"At the start of execution of the program, your program should print out:\n{expected}\nyour program printed out:\n{output}" )

    @points('2.working_with_numbers-part1')
    def test_2_count(self):
        for *inpt, count, sum, mean, p, n  in testset:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Input is asked too many times.") ],  ) as prompt:
                reload_module(self.module)
                output = get_stdout()
                expected = f'Numbers typed in {count}'
                self.assertFalse(len(output)==0, f"With the input\n{inpt}\nyour program should print out\n{expected}\nnow your program did not print out anything" )
                self.assertTrue(sanitize(expected) in sanitize(output), f"With the input\n{pp(inpt)}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    @points('2.working_with_numbers-part2')
    def test_3_sum(self):
        for *inpt, count, sum, mean, p, n  in  testset:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()
                expected = f'The sum of the numbers is {sum}'
                self.assertTrue(sanitize(expected) in sanitize(output), f"With the input\n{pp(inpt)}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    @points('2.working_with_numbers-part3')
    def test_4_mean(self):
        for *inpt, count, sum, mean, p, n in  testset: #[testset[0]]:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Input is asked too many times.") ], )  as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'The mean of the numbers is {mean}'
                self.assertTrue(sanitize(expected) in sanitize(output), f"With the input\n{pp(inpt)}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

    @points('2.working_with_numbers-part4')
    def test_5_posneg(self):
        for *inpt, count, sum, mean, p, n in  testset: #[testset[0]]:
            with patch('builtins.input', side_effect=[*inpt, AssertionError("Input is asked too many times.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  
                expected = f'Positive numbers {p}'
                self.assertTrue(sanitize(expected) in sanitize(output), f"With the input\n{pp(inpt)}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )
                expected = f'Negative numbers {n}'
                self.assertTrue(sanitize(expected) in sanitize(output), f"With the input\n{pp(inpt)}\nyour program should print out\n{expected}\nyour program printed out\n{output}" )

if __name__ == '__main__':
    unittest.main()