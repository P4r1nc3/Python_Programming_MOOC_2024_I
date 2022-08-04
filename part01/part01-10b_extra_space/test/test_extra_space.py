import unittest
from unittest.mock import patch
from inspect import getsource

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.extra_space'

expected = [
    "my name is Tim Tester, I am 20 years old",
    "",
    "my skills are",
    " - python (beginner)",
    " - java (veteran)",
    " - programming (semiprofessional)",
    "",
    "I am looking for a job with a salary of 2000-3000 euros per month"
]

@points('1.extra_space')
class ExtraSpaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        reload_module(self.module)
        output = get_stdout().split('\n')
        self.assertEqual(8, len(output), f"Your programs output contains incorrect amount of rows ({len(output)}), Output should contain exactly 8 rows. Make sure that you print also empty rows.")
        for i in range(0, 8):
            if i in [3, 4, 5]:
                self.assertEqual(' ', output[i][0], f"Output in row {i+1} is incorrect, Output was:\n{output[i]}\nPlease note that there is a space at the beginning of the row!")    
            self.assertEqual(expected[i], output[i].rstrip(), f"Output in row {i+1} is incorrect, it should be:\n{expected[i]}\nOutput was:\n{output[i]}")

    def test_print_2(self):
        prohibited = [
            "my name is Tim Tester, I am 20 years old",
            " - python (beginner)",
            " - java (veteran)",
            " - programming (semiprofessional)",
            "I am looking for a job with a salary of 2000-3000 euros per month"
        ]

        source = getsource(self.module)
        for line in source.split("\n"):
            for p in prohibited:
                if p in line:
                    self.assertTrue(False, f"Use values stored in variables when printing in program. Following row is not allowed in code\n{line}")

if __name__ == '__main__':
    unittest.main()
