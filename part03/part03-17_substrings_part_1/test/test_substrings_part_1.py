import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.substrings_part_1'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return "\n".join([s[0 : i] for i in range(1, len(s) + 1)])
   

@points('3.substrings_part_1')
class Substrings1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="auto"):
           cls.module = load_module(exercise, 'en')
    def test_short_strings(self):
        words = "auto ball candy motor hi it cap pizza dog".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works with the input {word}")
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)  
                self.assertTrue(len(output) == len(word), "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, len(word), len(output)))
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))
    
    def test_long_strings(self):
        words = "incomprehensibilities superlative absolutely supercalifragilisticexpialidocus".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"Make sure that your program works with the input {word}")
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)  
                self.assertTrue(len(output) == len(word), "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, len(word), len(output)))
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()
