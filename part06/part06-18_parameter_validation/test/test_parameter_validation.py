import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.parameter_validation'
function = 'new_person'

@points('6.parameter_validation')
class ParameterValidationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions should be included in the 
if __name__ == "__main__":
block. The following code should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.parameter_validation import new_person
        except:
            self.assertTrue(False, 'Your program should contain a function new_person(name: str, age: int)')

    def test_2_valid_values(self):
        test_cases = [("James Jameson", 32), ("Ann Anderson",11), ("Mary Puppins", 33), ("Tim Andrew Smith", 97), ("Matti Huuuhaa Innola", 145)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                new_person = load(exercise, function, 'en')
                try:
                    person = new_person(test_case[0], test_case[1])
                except ValueError:
                    self.assertTrue(False, f"Function threw an error with input {test_case}, although the parameter values are valid!")
                except:
                    self.assertTrue(False, f"Function failed to execute with input {test_case} - check the program code!")
                self.assertEqual(person, test_case, f"Function should return value {test_case} when input is {test_case} - now function returned {person}")

    def test_3_invalid_names(self):
        test_cases = [("Andrew", 32), ("",11), ("Mary", 33), ("Sirkka-Liisa Virtanen-Aftenbladet-Totterstrom-Lahtiska-Vanamo-Kullervoinen", 97)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                new_person = load(exercise, function, 'en')
                try:
                    person = new_person(test_case[0], test_case[1])
                    self.assertTrue(False, f"Function did not throw an error with input \n{test_case}\nalthough the parameters were invalid!")
                except ValueError:
                    pass

    def test_4_invalid_ages(self):
        test_cases = [("Andy Andyson", 232), ("Matt Matson",-11), ("Mary Poppers", 153)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
                reload_module(self.module)
                new_person = load(exercise, function, 'en')
                try:
                    person = new_person(test_case[0], test_case[1])
                    self.assertTrue(False, f"Function did not throw an error with input \n{test_case}\nalthough the parameters were invalid!")
                except ValueError:
                    pass

                
    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
