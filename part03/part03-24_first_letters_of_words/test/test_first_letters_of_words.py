import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.first_letters_of_words'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(s : str) -> str:
    return "\n".join([x[0] for x in s.split()])

@points('3.first_letters_of_words')
class FirstLettersOfWordsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = "x"):
           cls.module = load_module(exercise, 'en')

    def test_short_sentences(self):
        words = ["Ellohello", "Hi all", "Hey then everybody", "Simsalabim, magician said",
            "There is no rush for anything", "Here is one more sentence for test"]
        for testcase in words:
            with patch('builtins.input', return_value = testcase):
                try:
                    reload_module(self.module)
                except:
                     self.assertFalse(True, f"Make sure that the execution of the program works with the input\n{testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(testcase)
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + testcase)

                self.assertTrue(len(output) == len_correct, "Instead of {} rows, your program prints out {} rows with the input {}\n{}".
                    format(len_correct, len(output), testcase, output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input ({})".
                    format(output_all, correct, testcase))

    def test_longer_sentences(self):
        words = ['Once upon a time, a mouse, a bird, and a sausage, entered into partnership and set up house together.',
                'For a long time all went well: they lived in great comfort, and prospered so far as to be able to add considerably to their stores',
                'The bird’s duty was to fly daily into the wood and bring in fuel; the mouse fetched the water, and the sausage saw to the cooking.']
        for testcase in words:
            with patch('builtins.input', return_value = testcase):
                try:
                    reload_module(self.module)
                except:
                     self.assertFalse(True, f"Make sure that the execution of the program works with the input\n{testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(testcase)
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + testcase)

                self.assertTrue(len(output) == len_correct, "Instead of {} rows, your program prints out {} rows with the input {}\n{}".
                    format(len_correct, len(output), testcase, output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Your program's print out\n{}\ndoes not match with the correct print out \n{} \nwith the input ({})".
                    format(output_all, correct, testcase))

if __name__ == '__main__':
    unittest.main()