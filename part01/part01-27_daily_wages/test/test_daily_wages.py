import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.daily_wages'

@points('1.daily_wages')
class DailyWagesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0","0",""]):
            cls.module = load_module(exercise, 'en')

    def test_other_days_1(self):
        hours = randint(5,15)
        perhour = float(randint(10,25))
        test_input = "{},{},Tuesday".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Instead of one row, your program's output is now in {} rows".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "With input {} correct wage {} is not found in output {}".format(test_input, (hours * perhour), output))
            correct = "Daily wages: {} euros".format((hours * perhour))
            self.assertEqual(output, correct, "Print out is in incorrect format, correct print out is\n{}\nbut now print out is\n{}".format(correct,output))
    
    def test_other_days_2(self):
        hours = randint(5,15)
        perhour = float(randint(20,35))
        test_input = "{},{},Tuesday".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Instead of one row, your program's output is now in {} rows".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "With input {} correct wage {} is not found in output {}".format(test_input, (hours * perhour), output))
            correct = "Daily wages: {} euros".format((hours * perhour))
            self.assertEqual(output, correct, "Print out is in incorrect format, correct print out is\n{}\nbut now print out is\n{}".format(correct,output))
    
    def test_sunday_1(self):
        hours = randint(5,15)
        perhour = float(randint(10,25))
        test_input = "{},{},Sunday".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            perhour *= 2
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Instead of one row, your program's output is now in {} rows".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "With input {} correct wage {} is not found in output {}".format(test_input, (hours * perhour), output))
            correct = "Daily wages: {} euros".format((hours * perhour))
            self.assertEqual(output, correct, "Print out is in incorrect format, correct print out is\n{}\nbut now print out is\n{}".format(correct,output))
    
    def test_sunday_2(self):
        hours = randint(5,15)
        perhour = float(randint(10, 25))
        test_input = "{},{},Sunday".format(perhour, hours)
        ilist = test_input.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            perhour *= 2
            output_list = output.split("\n")
            self.assertTrue(len(output_list) == 1, "Instead of one row, your program's output is now in {} rows".format(len(output_list)))
            self.assertTrue(output.find(str(hours * perhour)) > -1, "With input {} correct wage {} is not found in output {}".format(test_input, (hours * perhour), output))
            correct = "Daily wages: {} euros".format((hours * perhour))
            self.assertEqual(output, correct, "Print out is in incorrect format, correct print out is\n{}\nbut now print out is\n{}".format(correct,output))
    

if __name__ == '__main__':
    unittest.main()
