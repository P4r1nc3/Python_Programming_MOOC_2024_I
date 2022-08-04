import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.loyalty_bonus'

@points('1.loyalty_bonus')
class LoyaltyBonusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def check(self,output,points,correct_points):
        check1 = output.find(str(correct_points)[:5]) > -1
        check2 = output.find(str(correct_points+1e-9)[:5]) > -1
        check3 = output.find(str(correct_points-1e-9)[:5]) > -1
        self.assertTrue(check1 or check2 or check3, "With input {} correct amount of points {} is not found in output {}".format(points, correct_points, output))

    def test_under_99(self):
        points = 99
        correct_points = 1.1 * points
        with patch('builtins.input', return_value = str(points)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "With input {} instead of two rows, your program did print out {} rows".format(points, len(output_list)))
            self.assertTrue(output.find("Your bonus is 10") > -1, "Row 'Your bonus is 10 %' was not found in output. Output was " + output)
            self.assertFalse(output.find("bonus is 15") > -1, "Output contained incorrect bonus-%, 15 %:', print out was " + output)
            self.check(output,points, correct_points)

    def test_under_100_random(self):
        points = randint(1,90)
        correct_points = 1.1 * points
        with patch('builtins.input', return_value = str(points)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "With input {} instead of two rows, your program did print out {} rows".format(points, len(output_list)))
            self.assertTrue(output.find("Your bonus is 10") > -1, "Row 'Your bonus is 10 %' was not found in output. Output was " + output)
            self.assertFalse(output.find("bonus is 15") > -1, "Output contained incorrect bonus-%, 15 %:', print out was " + output)
            self.check(output,points, correct_points)

    def test_100(self):
        points = 100
        correct_points = 1.15 * points
        with patch('builtins.input', return_value = str(points)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "With input {} instead of two rows, your program did print out {} rows".format(points, len(output_list)))
            self.assertTrue(output.find("Your bonus is 15") > -1, "Row 'Your bonus is 15 %' was not found in output. Output was " + output)
            self.assertFalse(output.find("bonus is 10") > -1, "Output contained incorrect bonus-%, 10 %:', print out was " + output)
            self.check(output,points, correct_points)

    def test_over_100_random(self):
        points = randint(101,1000)
        correct_points = 1.15 * points
        with patch('builtins.input', return_value = str(points)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 2, "With input {} instead of two rows, your program did print out {} rows".format(points, len(output_list)))
            self.assertTrue(output.find("Your bonus is 15") > -1, "Row 'Your bonus is 15 %' was not found in output. Output was " + output)
            self.assertFalse(output.find("bonus is 10") > -1, "Output contained incorrect bonus-%, 10 %:', print out was " + output)
            self.check(output,points, correct_points)
   
if __name__ == '__main__':
    unittest.main()
