import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.dictionary_file'
datafile = 'dictionary.txt'

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

def f(f):
    return "\n".join(f)

@points('6.dictionary_file')
class DictionaryFileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        clear_file()
        with patch('builtins.input', side_effect=["3"]):
           cls.module = load_module(exercise, 'en')

    def test_1_exit_only(self):
        input_data = ["3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            correct = "Bye"
            mssage = """\nNote, that in this exercise NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
            self.assertTrue(len(output.split("\n")) == 2, f"Program should output two lines with input\n{f(input_data)} now the output is \n{output}")
            self.assertTrue(correct in output, f"Program should output {correct} before stopping, now the output is \n{output}")

    def test_2_remove_add_words_and_exit (self):
        clear_file()
        input_data = ["1", "auto", "car", "3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            correct = "Bye"

            self.assertTrue(len(output.split("\n")) == 4, f"Program should output two lines with input\n{f(input_data)} now the output is \n{output}")
            self.assertTrue(correct in output, f"Program should output {correct} before stopping, now the output is \n{output}")


    def test_3_remove_add_words_and_output(self):
        clear_file()
        input_data = ["1", "tietokone", "computer", "2", "tietokone", "3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            
            correct = "tietokone - computer"
            self.assertTrue(correct in output, f"With input:\n{f(input_data)}\nthe program should output \n{correct}\nnow the output is \n{output}")

    def test_4b_load_again_and_output(self):
        input_data1 = ["1", "tietokone", "computer", "2", "tietokone", "3"]
        input_data = ["2", "tietokone", "3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            
            correct = "tietokone - computer"
            self.assertTrue(correct in output, f"When the program is first executed with input data\n{f(input_data1)}\nand again with input data:\n{f(input_data)}\not should output \n{correct}\nnow it outputs \n{output}")

    def test_5_add_words_and_output(self):
        input_data1 = ["1", "tietokone", "computer", "3"]
        input_data = ["1", "tieto", "knowledge", "1", "tietoisuus", "conscience", "2", "tieto","3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            
            corrects = ["tietokone - computer", "tieto - knowledge", "tietoisuus - conscience"]
            for correct in corrects:
                self.assertTrue(correct in output, f"When the program is first executed with input data\n{f(input_data1)}\nand again with input data:\n{f(input_data)}\nthe output should containt \n{correct}\nnow it outputs \n{output}")

    def test_6_add_words_and_output_en(self):
        clear_file()
        input_data = ["1", "uida", "swim", "1", "uimari", "swimmer", "1", "uimapuku", "swimsuit", "2", "swim", "3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            
            corrects = ["uida - swim", "uimari - swimmer", "uimapuku - swimsuit"]
            for correct in corrects:
                 self.assertTrue(correct in output, f"When the program is first executed  with input data:\n{f(input_data)}\nothe output should contain \n{correct}\nnow it outputs \n{output}")

    def test_7_output_1(self):
        input_data1 = ["1", "uida", "swim", "1", "uimari", "swimmer", "1", "uimapuku", "swimsuit", "3"]
        input_data = ["2", "swim", "3"]
        with patch('builtins.input', side_effect=input_data):
            try:
                reload_module(self.module)
            except:
                self.fail(f"Ensure that program can be executed with input:\n{f(input_data)}")
            output = get_stdout()
            
            corrects = ["uida - swim", "uimari - swimmer", "uimapuku - swimsuit"]
            for correct in corrects:
                self.assertTrue(correct in output, f"When the program is first executed with input data\n{f(input_data1)}\nand again with input data:\n{f(input_data)}\nthe output should contain \n{correct}\nnow it outputs \n{output}")

if __name__ == '__main__':
    unittest.main()
