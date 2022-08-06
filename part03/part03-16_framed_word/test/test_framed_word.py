import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce

exercise = 'src.framed_word'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return sanitize(str1.lower()) == sanitize(str2.lower())

def get_correct(s : str) -> str:
    s1 = "*" * 30
    s2 = "*" + (28 - len(s)) // 2 * " " + s + (28 -len(s)) // 2 * " "
    if len(s) % 2 == 1:
        s2 += " "
    return s1 + "\n" + s2 + "*\n" + s1
   
def get_correct2(s : str) -> str:
    s1 = "*" * 30
    s2 = (28 - len(s)) // 2 * " " + s + (28 -len(s)) // 2 * " "
    if len(s) % 2 == 1:
        s2 = " " + s2
    return s1 + "\n*" + s2 + "*\n" + s1

@points('3.framed_word')
class FramedWordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="a"):
           cls.module = load_module(exercise, 'en')

    def test_short_words(self):
        words = "test! helloh simsalabim zorro yeah!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 3, "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, 3, len(output)))

                self.assertEqual(output[0], "*" * 30, "First row of your print out does not consist of 30 stars: {}".format(output[0]))
                self.assertEqual(output[2], "*" * 30, "Last row of your print out does not consist of 30 stars: {}".
                    format(output[2]))

                self.assertTrue(len(output[1]) == 30, "Length of middle row is {}, instead of 30, when input is {}: \n{}".
                    format(len(output[1]), word, output[1]))

                correct2 = get_correct2(word)
                self.assertTrue(outputs_equal(output_all, correct) or outputs_equal(output_all, correct2), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

    def test_long_words(self):
        words = ["This is a longer sentence.", "simsalabim, magician said", "123456789012345678901234567", "abcdefgacbdefg"]
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)
                self.assertTrue(len(output) == 3, "With the input {}, instead of {} rows, your program's print out is in {} rows".
                    format(word, 3, len(output)))

                self.assertEqual(output[0], "*" * 30, "First row of your print out does not consist of 30 stars: {}".format(output[0]))
                self.assertEqual(output[2], "*" * 30, "Last row of your print out does not consist of 30 stars: {}".
                    format(output[2]))

                self.assertTrue(len(output[1]) == 30, "Length of middle row is {}, instead of 30, when input is {}: \n{}".
                    format(len(output[1]), word, output[1]))
                
                correct2 = get_correct2(word)
                self.assertTrue(outputs_equal(output_all, correct) or outputs_equal(output_all, correct2), "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()
