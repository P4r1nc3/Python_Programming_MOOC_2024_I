import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.course_grading_part_1'

def f(d):
    return '\n'.join(d)

def w(x):
    return [f"test/{i}" for i in x]

import os
from shutil import copyfile


@points('6.course_grading_part_1')
class CourseGradingPart1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['test/students1.csv', 'test/exercises1.csv', 'third']):
           cls.module = load_module(exercise, 'en')

    def test_1_works_with_files_1(self):
        words = ['students1.csv', 'exercises1.csv']
        with patch('builtins.input', side_effect = w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your progaram can be executed with\n{f(words)}")
        
            exp = """pekka peloton 21
jaana javanainen 27
liisa virtanen 35"""
            expRows = exp.split('\n')


            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
            
            self.assertTrue(len(output_all)>0, f"Your program doesn't output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should be:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work with input\n{f(words)}\nrow {line} is not what was expected\nTThe output should contain the following lines:\n{exp}\nWhole output is:\n{output_all}")

    def test_2_works_with_files_2(self):
        words = ['students2.csv', 'exercises2.csv']
        with patch('builtins.input', side_effect = w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your progaram can be executed with\n{f(words)}")
        
            exp = """pekka peloton 25
jaana javanainen 27
liisa virtanen 35
donald frump 0
john doe 28
angela tarkel 32
karkki eila 30
alan turing 28
ada lovelace 17"""
            expRows = exp.split('\n')


            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
            
            self.assertTrue(len(output_all)>0, f"Your program doesn't output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should be:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work with input\n{f(words)}\nrow {line} is not what was expected\nTThe output should contain the following lines:\n{exp}\nWhole output is:\n{output_all}")


  
    def test_3_works_with_files_3(self):
        words = ['students3.csv', 'exercises3.csv']
        with patch('builtins.input', side_effect = w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your progaram can be executed with\n{f(words)}")
        
            exp = """pekka peloton 25
jaana javanainen 30
liisa virtanen 34
donald frump 40
john doe 36
angela tarkel 16
karkki eila 26
alan turing 24
ada lovelace 26"""
            expRows = exp.split('\n')


            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
            
            self.assertTrue(len(output_all)>0, f"Your program doesn't output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should be:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work with input\n{f(words)}\nrow {line} is not what was expected\nTThe output should contain the following lines:\n{exp}\nWhole output is:\n{output_all}")

    def test_4_works_with_files_4(self):
        words = ['students4.csv', 'exercises4.csv']
        with patch('builtins.input', side_effect = w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your progaram can be executed with\n{f(words)}")
        
            exp = """pekka pelokas 25
mirja virtanen 30
jane doe 33
donald frump 35
john doe 36
kalle paakkola 16
eila kaisla 29
antti tuuri 18
leena lempinen 26
eero honkela 21"""
            expRows = exp.split('\n')


            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
            
            self.assertTrue(len(output_all)>0, f"Your program doesn't output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should be:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work with input\n{f(words)}\nrow {line} is not what was expected\nTThe output should contain the following lines:\n{exp}\nWhole output is:\n{output_all}")


  
  
if __name__ == '__main__':
    unittest.main()
