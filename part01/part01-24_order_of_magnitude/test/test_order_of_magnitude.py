import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.order_of_magnitude'

@points('1.order_of_magnitude')
class OrderOfMagnitudeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        number = 9
        with patch('builtins.input', return_value = str(number)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if number < 1000:
                self.assertEqual(output[0].strip(), "This number is smaller than 1000", "Your program did not print out\nThis number is smaller than 1000\nFor number " + str(number))
            if number < 100:
                self.assertTrue(len(output)>1, "Your program did not print out\nThis number is smaller than 100\nFor number " + str(number))
                self.assertEqual(output[1].strip(), "This number is smaller than 100", "Your program did not print out\nThis number is smaller than 100\nFor number " + str(number))
            if number < 10:
                self.assertTrue(len(output)>2, "Your program did not print out\nThis number is smaller than 10\nFor number " + str(number))
                self.assertEqual(output[2].strip(), "This number is smaller than 10", "Your program did not print out\nThis number is smaller than 10\nFor number " + str(number))
            self.assertEqual(output[-1], "Thank you!", "At the end of the execution of the program, your program did not print out row 'Thank you!'")

    def test_print_2(self):
        number = 97
        with patch('builtins.input', return_value = str(number)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if number < 1000:
                self.assertEqual(output[0], "This number is smaller than 1000", "Your program did not print out that number is smaller than 1000 for number " + str(number))
            if number < 100:
                self.assertTrue(len(output)>1, "Your program did not print out\nThis number is smaller than 100\nFor number " + str(number))
                self.assertEqual(output[1], "This number is smaller than 100", "Your program did not print out that number is smaller than 100 for number " + str(number))
            if number < 10:
                self.assertTrue(len(output)>2, "Your program did not print out\nThis number is smaller than 10\nFor number " + str(number))
                self.assertEqual(output[2], "This number is smaller than 10", "Your program did not print that number is smaller than 10 for number " + str(number))
            self.assertEqual(output[-1], "Thank you!", "At the end of the execution of the program, your program did not print row 'Thank you!'")

    def test_print_3(self):
        number = 451
        with patch('builtins.input', return_value = str(number)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if number < 1000:
                self.assertEqual(output[0], "This number is smaller than 1000", "Your program did not print out that number is smaller than 1000 for number " + str(number))
            if number < 100:
                self.assertTrue(len(output)>1, "Your program did not print out\nThis number is smaller than 100\nFor number " + str(number))
                self.assertEqual(output[1], "This number is smaller than 100", "Your program did not print out that number is smaller than 100 for number " + str(number))
            if number < 10:
                self.assertTrue(len(output)>2, "Your program did not print out\nThis number is smaller than 10\nFor number " + str(number))
                self.assertEqual(output[2], "This number is smaller than 10", "Your program did not print that number is smaller than 10 for number " + str(number))
            self.assertEqual(output[-1], "Thank you!", "At the end of the execution of the program, your program did not print row 'Thank you!'")

    def test_print_4(self):
        number = 111234
        with patch('builtins.input', return_value = str(number)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if number < 1000:
                self.assertEqual(output[0], "This number is smaller than 1000", "Your program did not print out that number is smaller than 1000 for number " + str(number))
            if number < 100:
                self.assertTrue(len(output)>1, "Your program did not print out\nThis number is smaller than 100\nFor number " + str(number))
                self.assertEqual(output[1], "This number is smaller than 100", "Your program did not print out that number is smaller than 100 for number " + str(number))
            if number < 10:
                self.assertTrue(len(output)>2, "Your program did not print out\nThis number is smaller than 10\nFor number " + str(number))
                self.assertEqual(output[2], "This number is smaller than 10", "Your program did not print that number is smaller than 10 for number " + str(number))
            self.assertEqual(output[-1], "Thank you!", "At the end of the execution of the program, your program did not print row 'Thank you!'")

if __name__ == '__main__':
    unittest.main()
