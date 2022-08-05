import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.number_of_characters'

@points('2.number_of_characters')
class NumberOfCharactersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'en')

    def test_long_words(self):
        words = "auto helicopter airplane moped bicycle".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anythin with input "  +word)
                self.assertTrue(len(output) == 2, "With input {}, instead of two rows, your program's output is in {} rows".format(word, len(output)))
                self.assertTrue(output[0].find(str(len(word))) > -1, "Your program's output\n{}\ndoes not contain correct number of characters {} with input {}".format(output[0], len(word), word))
                self.assertEqual(sanitize(output[1]), "Thank you!", "At the end of the execution of the program, your program did not print out row 'Thank you! with input " +word)

    def test_single_character(self):
        words = "a X z".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anythin with input "  +word)
                self.assertTrue(len(output) == 1, "With input {}, instead of two rows, your program's output is in {} rows".format(word, len(output)))
                self.assertEqual(sanitize(output[0]), "Thank you!", "At the end of the execution of the program, your program did not print out row 'Thank you! with input " +word)
   
if __name__ == '__main__':
    unittest.main()
