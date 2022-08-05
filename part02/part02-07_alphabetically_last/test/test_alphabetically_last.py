import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.alphabetically_last'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.alphabetically_last')
class AlphabeticallyLastTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0']):
            cls.module = load_module(exercise, 'en')

    def test_1_first_one_comes_last(self):
        values = [("def","abc"), ("aardwolf", "aardvark"), ("watch", "wasp")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Remove headers
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "From the output {} alphabetically last word {} is not found when input is {}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))

    def test_2_second_one_comes_last(self):
        values = [("automat","autonomous"), ("lounge", "love"), ("abcde", "xyz")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Remove headers
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[1]) > -1, "From the output {} alphabetically last word {} is not found when input is {}".
                    format(output[0], valuegroup[1], format_tuple(valuegroup)))

    def test_3_equal_ones(self):
        values = [("test","test"), ("flower", "flower"), ("abcdefg", "abcdefg")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Remove headers
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "After asking the inputs from user, instead of one row, your program's output is in {} rows: {} with input:\n{}".
                    format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find("same word twice") > -1, "Output {} does not contain mention 'You gave the same word twice' when input is {}".
                    format(output[0], format_tuple(valuegroup)))

if __name__ == '__main__':
    unittest.main()
