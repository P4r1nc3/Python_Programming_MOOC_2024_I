import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.print_numbers'

@points('2.print_numbers')
class PrintNumbersTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.module = load_module(exercise, 'en')

        def test_print_numbers(self):
            reload_module(self.module)
            output = get_stdout()
            output_list = [x for x in output.split("\n") if len(x.strip()) > 0]
            cor = [str(x) for x in range(2,31,2)]
            self.assertEqual(len(output_list), 15, f"Your program is expected to print out 15 rows, now print out is in {len(output_list)} rows.")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1, l2, f"Print out in row {r+1} does not match with the model solution: program should print out {l1}, but it prints out {l2}.")

if __name__ == '__main__':
    unittest.main()