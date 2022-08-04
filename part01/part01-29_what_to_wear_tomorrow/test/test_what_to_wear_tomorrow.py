import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.what_to_wear_tomorrow'

jeans_tshirt = "Wear jeans and a T-shirt"
jumper = "I recommend a jumper as well"
jacket = "Take a jacket with you"
warm_coat = "Make it a warm coat, actually"
gloves = "I think gloves are in order"
umbrella = "Don't forget your umbrella!"

@points('1.what_to_wear_tomorrow')
class WhatToWearTomorrowTest(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_25(self):
        with patch('builtins.input', side_effect = [ '25', 'no', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "25, no"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jumper in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jacket in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertFalse(warm_coat in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertFalse(gloves in output, f"With input:\n{input}\nohjelmanEI pitäisi tulostaa riviä\n" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertFalse(umbrella in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_21_rain(self):
        with patch('builtins.input', side_effect = [ '21', 'yes', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "21, yes"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jumper in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jacket in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertFalse(warm_coat in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertFalse(gloves in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertTrue(umbrella in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_15(self):
        with patch('builtins.input', side_effect = [ '15', 'no', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "15, no"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jumper in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jacket in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertFalse(warm_coat in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertFalse(gloves in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertFalse(umbrella in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_20_rain(self):
        with patch('builtins.input', side_effect = [ '20', 'yes', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "20, yes"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jumper in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertFalse(jacket in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertFalse(warm_coat in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertFalse(gloves in output, f"With input:\n{input}\nprogram is NOT expected to print out following rown" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertTrue(umbrella in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_10(self):
        with patch('builtins.input', side_effect = [ '10', 'no', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "10, no"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jumper in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jacket in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertFalse(warm_coat in output, f"With input:\n{input}\nprogram is NOT expected to print out following row\n" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertFalse(gloves in output, f"With input:\n{input}\nprogram is NOT expected to print out following row\n" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertFalse(umbrella in output, f"With input:\n{input}\nprogram is NOT expected to print out following row\n" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_3(self):
        with patch('builtins.input', side_effect = [ '3', 'no', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "3, no"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jumper in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jacket in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertTrue(warm_coat in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertTrue(gloves in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertFalse(umbrella in output, f"With input:\n{input}\nprogram is NOT expected to print out following row\n" + umbrella+ "\nyour program's print out is\n"+ output)
    
    def test_5_rain(self):
        with patch('builtins.input', side_effect = [ '5', 'yes', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            input = "5, yes"
            self.assertFalse(prompt.call_count < 1, 'Program must ask for input two times.')
            self.assertTrue(jeans_tshirt in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jeans_tshirt+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jumper in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jumper+ "\nyour program's print out is\n"+ output)
            self.assertTrue(jacket in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + jacket+ "\nyour program's print out is\n"+ output)
            self.assertTrue(warm_coat in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + warm_coat+ "\nyour program's print out is\n"+ output)
            self.assertTrue(gloves in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + gloves+ "\nyour program's print out is\n"+ output)
            self.assertTrue(umbrella in output, f"With input:\n{input}\nprogram is expected to print out following row\n" + umbrella+ "\nyour program's print out is\n"+ output)
    

if __name__ == '__main__':
    unittest.main()
