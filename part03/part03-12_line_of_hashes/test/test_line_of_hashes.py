import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.line_of_hashes'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return int(s) * "#"
   

@points('3.line_of_hashes')
class LineOfHashesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="3"):
           cls.module = load_module(exercise, 'en')


    def test_short(self):
        words = "5 3 2 6 1".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 1, "With the input {} instead of {} rows your program's print out is in {} rows".
                    format(word, 1, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

    def test_long(self):
        words = "15 13 22 16 10".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 1, "With the input {} instead of {} rows your program's print out is in {} rows".
                    format(word, 1, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))
    
    

    
    

if __name__ == '__main__':
    unittest.main()
