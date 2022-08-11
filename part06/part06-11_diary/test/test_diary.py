import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.diary'
datafile = 'diary.txt'

def get_correct() -> dict:
    pass

def clear_file():
    with open(datafile, "w"):
        pass

def get_content():
    with open(datafile) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

def format(f):
    return "\n".join(f)

@points('6.diary')
class DiaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        clear_file()
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'en')

    def test_1_exit_only(self):
        input_value = "0"
        with patch('builtins.input', side_effect=["0"]):
            reload_module(self.module)
            output = get_stdout()
            correct = "Bye now"

            mssage = """\nPlease note, that in this exercise NO CODE should be included in the
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.assertFalse(len(output) == 0, f"Your program should output two lines with input\n{input_value}\nNow it outputs nothing\n{mssage}") 
            self.assertTrue(len(output.split("\n")) == 2, f"Your program should output two lines with input\n{input_value}\nNow it outputs \n{output}")
            self.assertTrue(correct in output, f"Program should output {correct}, now the output is \n{output}")

    def test_2_add_line_and_exit(self):
        clear_file()
        with patch('builtins.input', side_effect=["1", "I woke up at nine", "0"]):
            reload_module(self.module)
            output = get_stdout()
            
            content = get_content()
            correct = ["I woke up at nine"]
            input_value = "\n".join(["1", "I woke up at nine", "0"])

            self.assertTrue(len(content) > 0, f"If the file was empty, with input\n{input_value}\ntthe file should now contain a single line. The file, however, is empty.")
            self.assertTrue(len(content) == len(correct), f"If the file was empty, with input\n{input_value}\ntthe file should now contain a single line. The content of the file is:\n{format(content)}")
            self.assertEqual(content, correct, f"If the file was empty at first, with input\n{input_value} \nthe content of the file should be \n{format(correct)}\nbut instead it is \n{format(content)}")

    def test_3_clear_add_2_lines_and_exit(self):
        clear_file()
        with patch('builtins.input', side_effect=["1", "Today was hot", "1", "I learned more Python", "0"]):
            reload_module(self.module)
            output = get_stdout()
            
            input_values = "\n".join(["1", "Today was hot", "1", "I learned more Python", "0"])

            content = get_content()
            correct = ["Today was hot", "I learned more Python"]

            self.assertTrue(len(content) == len(correct), f"If file was empty at first, with input\n{input_values}\nthe file should now contain 2 lines:\n{format(correct)}\nThe content is\n{format(content)}")
            self.assertEqual(content, correct, f"If file was empty at first, with input value\n{input_values}\nthe content of the file should be \n{format(correct)}\nbut instead it is\n{format(content)}")

    def test_4_output_content(self):
        with patch('builtins.input', side_effect=["2", "0"]):
            reload_module(self.module)
            output = get_stdout().split("\n")
            output = [x.strip() for x in output if "1 - " not in x and "ye now" not in x and not "tries" in x]
            output = [x for x in output if len(x)>0]

            correct = ["Today was hot", "I learned more Python"]

            syote1 = "\n".join(["1", "Today was hot", "1", "I learned more Python", "0"])
            syote = "\n".join(["2", "0"])

            self.assertTrue(len(output)>0, f"When the program is first executed with input\n{syote1}\nand then restarted and executed with input:\n{syote}\nthe program should output entries\n{format(correct)}\nbut it does not output any entries")
            self.assertTrue(output == correct, f"When the program is first executed with input\n{syote1}\nand then restarted and executed with input:\n{syote}\nthe program should output entries\n{format(correct)}\nInstead it outputs:\n{format(output)}")
    

   
if __name__ == '__main__':
    unittest.main()
