import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.rectangle_of_hashes'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    w, h = s[1:-1].split(",")
    return "\n".join([(int(w) * "#") for i in range(int(h))])
   

@points('3.rectangle_of_hashes')
class RectangleOfHashesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["1","1"]):
           cls.module = load_module(exercise, 'en')


    def test_1_small_symmetric(self):
        words = "(2,2) (5,5) (3,3) (6,6) (1,1)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output[0]) == w, f"With the input {word} width of the rectangle should be {w}, it was {len(output[0])}. Your program's output:\n{output_all}")
                self.assertTrue(len(output) == h, f"With the input {word} height of the rectangle should be {h}, it was {len(output)}. Your program's output:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))
    
    def test_2_big_symmetric(self):
        words = "(10,10) (15,15) (8,8)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output[0]) == w, f"With the input {word} width of the rectangle should be {w}, it was {len(output[0])}. Your program's output:\n{output_all}")
                self.assertTrue(len(output) == h, f"With the input {word} height of the rectangle should be {h}, it was {len(output)}. Your program's output:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

    def test_3_not_symmetric(self):
        words = "(5,3) (3,6) (8,4) (5,10)".split(" ")
        for word in words:
            with patch('builtins.input', side_effect = word[1:-1].split(",")):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
                w, h = [int(x) for x in word[1:-1].split(",")]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output[0]) == w, f"With the input {word} width of the rectangle should be {w}, it was {len(output[0])}. Your program's output:\n{output_all}")
                self.assertTrue(len(output) == h, f"With the input {word} height of the rectangle should be {h}, it was {len(output)}. Your program's output:\n{output_all}")
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()