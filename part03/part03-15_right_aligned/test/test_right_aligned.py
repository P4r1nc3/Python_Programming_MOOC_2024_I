import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.right_aligned'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return (20 - len(s)) * "*" + s
   

@points('3.right_aligned')
class RightAlignedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="3"):
           cls.module = load_module(exercise, 'en')

    def test_short_words(self):
        words = "test hiya simsalabim zorro woo-hoo!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input " + word)
                self.assertTrue(len(output) == 1, "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, 1, len(output)))
                self.assertTrue(output_all.count("*") == 20 - len(word), "Instead of correct amount of stars ({}) your program prints out {} stars, with the input {}: \n{}".
                    format((20 - len(word)), output_all.count("*"), word, output_all))
                self.assertTrue(len(output_all) == 20, "Instead of 20 characters, length of your print out is {} characters. Print out was:\n{}\nExpected print out was\n{}".format(len(output_all), output_all, correct))
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out\n{}\nwith the input {}".
                    format(output_all, correct, word))

    def test_long_sanat(self):
        words = "rockingchairshop verylongcombination abcdefghijkl almost20characters!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input " + word)
                self.assertTrue(len(output) == 1, "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, 1, len(output)))
                self.assertTrue(output_all.count("*") == 20 - len(word), "Instead of correct amount of stars ({}) your program prints out {} stars, with the input {}: \n{}".
                    format((20 - len(word)), output_all.count("*"), word, output_all))
                self.assertTrue(len(output_all) == 20, "Instead of 20 characters, length of your print out is {} characters. Print out was:\n{}\nExpected print out was\n{}".format(len(output_all), output_all, correct))
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out\n{}\nwith the input {}".
                    format(output_all, correct, word))

if __name__ == '__main_':
    unittest.main()