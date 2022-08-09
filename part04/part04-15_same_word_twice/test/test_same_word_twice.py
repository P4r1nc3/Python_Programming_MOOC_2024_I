import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.same_word_twice'

def f(d):
    return '\n'.join(d)
 
@points('4.same_word_twice')
class SameWordTwiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["python", "test","python"]):
            cls.module = load_module(exercise, 'en')

    def test_1_program_stops(self):
        words = "python test python".split(" ")
    
        with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure that the execution of the program stops with the input\n{f(words)}")

    def test_2_functionality_ok(self):
        for string in [
                "python test python",
                "there was vscode tmc and jack at start here was",
                "once upon a time there was programmer upon",
                "first second third fourth fifth second",
                "bug bug",
                "code works well when its coded well",
                "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua elit"
            ]:
            words = string.split(" ")
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Make sure that the execution of the program stops with the input\n{f(words)}")

                mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
                """
                #\n{mssage}")     
                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}\n{mssage}")  
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(1, len(output), f"Instead of one row, your programs print out is now in {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}")
                correct = "You typed in "+str(len(words)-1)+" different words"
                self.assertTrue(output[0].rstrip() == correct, f"The print out of your program is incorrect, it should be\n{correct}\nrow is\n{output[0]}\nwhen the input is:\n{f(words)}")

if __name__ == '__main__':
    unittest.main()