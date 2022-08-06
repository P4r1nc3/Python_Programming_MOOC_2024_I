import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.second_and_second_to_last'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

@points('3.second_and_second_to_last')
class SecondAndSecondToLastTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="word"):
           cls.module = load_module(exercise, 'en')

    def test_same(self):
        words = "pascal never tom-tom racecar madam book otto abccba pip hut saw odd state xyzzzzyz".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program's works with the input {word}")
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = "The second and the second to last characters are " + word[1]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 1, "With the input {} instead of one row, your program's print out is in {} rows".format(word, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Your program's print out\n{}\ndoes not match with the correct print out\n{} \nwith the input {}".
                    format(output[0], correct, word))

    def test_different(self):
        words = "python java cake xyxy test abbab cottages longertest".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program's works with the input {word}")
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = "The second and the second to last characters are different"
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 1, "With the input {} instead of one row, your program's print out is in {} rows".format(word, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Your program's print out\n{}\ndoes not match with the correct print out\n{} \nwith the input {}".
                    format(output[0], correct, word))
    

if __name__ == '__main__':
    unittest.main()