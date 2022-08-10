import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.numbers_spelled_out'
function = 'dict_of_numbers'

def get_correct() -> dict:
    return {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 21: 'twenty-one', 22: 'twenty-two', 23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five',
    26: 'twenty-six', 27: 'twenty-seven', 28: 'twenty-eight', 29: 'twenty-nine', 30: 'thirty', 31: 'thirty-one', 32: 'thirty-two',
    33: 'thirty-three', 34: 'thirty-four', 35: 'thirty-five', 36: 'thirty-six', 37: 'thirty-seven', 38: 'thirty-eight', 39: 'thirty-nine',
    40: 'forty', 41: 'forty-one', 42: 'forty-two', 43: 'forty-three', 44: 'forty-four', 45: 'forty-five', 46: 'forty-six', 47: 'forty-seven',
    48: 'forty-eight', 49: 'forty-nine', 50: 'fifty', 51: 'fifty-one', 52: 'fifty-two', 53: 'fifty-three', 54: 'fifty-four', 55: 'fifty-five',
    56: 'fifty-six', 57: 'fifty-seven', 58: 'fifty-eight', 59: 'fifty-nine', 60: 'sixty', 61: 'sixty-one', 62: 'sixty-two', 63: 'sixty-three',
    64: 'sixty-four', 65: 'sixty-five', 66: 'sixty-six', 67: 'sixty-seven', 68: 'sixty-eight', 69: 'sixty-nine', 70: 'seventy',
    71: 'seventy-one', 72: 'seventy-two', 73: 'seventy-three', 74: 'seventy-four', 75: 'seventy-five', 76: 'seventy-six', 77: 'seventy-seven',
    78: 'seventy-eight', 79: 'seventy-nine', 80: 'eighty', 81: 'eighty-one', 82: 'eighty-two', 83: 'eighty-three', 84: 'eighty-four',
    85: 'eighty-five', 86: 'eighty-six', 87: 'eighty-seven', 88: 'eighty-eight', 89: 'eighty-nine', 90: 'ninety', 91: 'ninety-one',
    92: 'ninety-two', 93: 'ninety-three', 94: 'ninety-four', 95: 'ninety-five', 96: 'ninety-six', 97: 'ninety-seven', 98: 'ninety-eight', 99: 'ninety-nine'}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.numbers_spelled_out')
class NumbersSpelledOutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.numbers_spelled_out import dict_of_numbers
        except:
            self.assertTrue(False, 'Your code should contain function named as dict_of_numbers')
        try:
            dict_of_numbers()
        except:
            self.assertTrue(False, 'Make sure, that following function call works: dict_of_numbers()')

    def test_2_type_of_return_value(self):
        dict_of_numbers = load(exercise, function, 'en')
        val = dict_of_numbers()
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Function {function} should return dictionary, now it returns value which is {taip} type")

    def test_3_numbers(self):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            reload_module(self.module)
            output_at_start = get_stdout()
            dict_of_numbers = load(exercise, function, 'en')

            numbers = dict_of_numbers()

            self.assertEqual(100, len(numbers), f"The dictionary returned should contain 100 itmes, but it contains {len(numbers)} items: \n{numbers}")

            tests = get_correct()
            for i in range(100):
                self.assertEqual(tests[i], numbers[i], f"Sanakirjan arvoThe value {numbers[i]} in dictionary does not match with the model solution {tests[i]} with key value {i}")

if __name__ == '__main__':
    unittest.main()
