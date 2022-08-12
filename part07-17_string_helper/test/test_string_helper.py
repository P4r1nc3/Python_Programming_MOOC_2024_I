import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.string_helper'
functions = "change_case split_in_half remove_special_characters".split()



@points('7.string_helper')
class StringHelperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)


    def test1_module_exists(self):
        try:
            import src.string_helper
        except:
            self.assertTrue(False, "Your solution should have a module named string_helper.py defined")

    def test2_functions_exists(self):
        try:
            from src.string_helper import change_case, split_in_half, remove_special_characters
        except:
            self.assertTrue(False, "The functions change_case, split_in_half ja remove_special_characters should be found from the string_helper module")
    
    def test3_test_change_case(self):
        test_cases = {"aaa": "AAA", "abcdef": "ABCDEF", "testing": "TESTING", "two different words": "TWO DIFFERENT WORDS",
                      "YYY": "yyy", "ABCXYZ": "abcxyz", "TESTWORD": "testword", "SEVERAL WORDS": "several words",
                      "AAAaaa": "aaaAAA", "AaBbCcXxYyZz": "aAbBcCxXyYzZ", "Test With SevErAl WoRDs": "tEST wITH sEVeRaL wOrdS",
                      "HoW AbOuT ThiS": "hOw aBoUt tHIs", "I am THE boogeyman": "i AM the BOOGEYMAN"}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                change_case = load(exercise, functions[0], 'en')
                try:
                    val = change_case(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Calling change_case with the parameter {test_case} caused an error.")

                self.assertTrue(type(val) == str, f"Function change_case should return a value whichs type is str when it is called with the parameter {test_case}, now function returned a value {val}, whichs type is {taip}")
                self.assertEqual(val, correct, f"Calling change_case returns a value '{val}' with the paramater value '{test_case}' when the correct answer would have been {correct}")

    def test4_test_split_in_half(self):
        test_cases = {"abcd": ("ab", "cd"), "ab": ("a", "b"), "111222":("111","222"), "onetwo": ("one","two"), 
                      "abcdefg": ("abc", "defg"), "123456789": ("1234", "56789"), "abracadabra": ("abrac", "adabra")}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                split_in_half = load(exercise, functions[1], 'en')

                try:
                    val = split_in_half(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Calling split_in_half with the parameter {test_case} caused an error.")

                self.assertTrue(type(val) == tuple, f"Funktion split_in_half pitäisi palauttaa arvo tyyppiä tuple kun sitä kutsutaan parametrilla {test_case}, now function returned a value {val}, whichs type is {taip}")
                self.assertTrue(len(val) == 2, f"Calling split_in_half is expected to return two strings in a tuple, but now the return value was {val}")
                self.assertEqual(val, correct, f"Calling split_in_half returns a value '{val}' with the paramater value '{test_case}' when the correct answer would have been {correct}")

    
    def test5_test_remove_special_characters(self):
        test_cases = {"hey!": "hey", "Thi§ is a test: test?": "Thi is a test test", "Oh nooooo!!!!111": "Oh nooooo111",
                      "a,b.c;d:e_f*g!h#i¤j%k&l/m(n)": "abcdefghijklmn", "(1+3)*2=8": "1328", "Nothing is removed from this": "Nothing is removed from this"}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                remove_special_characters = load(exercise, functions[2], 'en')

                try:
                    val = remove_special_characters(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Calling remove_special_characters with the parameter {test_case} caused an error")

                self.assertTrue(type(val) == str, f"Function remove_special_characters should return a value whichs type is str when it is called with the parameter {test_case}, now function returned a value {val}, whichs type is {taip}")
                self.assertEqual(val, correct, f"Calling remove_special_characters returns a value '{val}' with the paramater value '{test_case}' when the correct answer would have been {correct}")

if __name__ == '__main__':
    unittest.main()