import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.grades_and_points'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def get_grade(p : int) -> str:
    if p == 100:
        return "5"
    return str((p - 50) // 10 + 1)

@points('2.grades_and_points')
class GradesAndPointsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1_negatives(self):
        values = [str(randint(-1000,-1)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("impossible!") > -1, "From output\n{}\nmention 'impossible!' is not found when input is {}".
                    format(output[0], value))

    def test_2_too_high(self):
        values = [str(randint(101,10000)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("impossible!") > -1, "From output\n{}\nmention 'impossible!' is not found when input is {}".
                    format(output[0], value))

    def test_3_fails(self):
        values = [str(randint(0,49)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("fail") > -1, "From output\n{}\nmention 'fail' is not found when input is {}".
                    format(output[0], value))

    def test_0_grades(self):
        values = "50 55 59 60 67 69 70 79 80 89 90 99 100".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is now in {} rows: {} when input is {}".format(len(output), output, value))
                correct = "Grade: " + get_grade(int(value))
                self.assertEqual(output[0].strip(), correct, "Output\n{}\ndoes not match with correct output\n{}\nwhen input is {}".
                    format(output[0], correct, value))
                
if __name__ == '__main__':
    unittest.main()
