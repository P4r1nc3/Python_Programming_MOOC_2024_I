import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.course_grading_part_2'

def f(d):
    return '\n'.join(d)
    
def w(x):
    return [f"test/{i}" for i in x]

@points('6.course_gradind_part_2')
class CourseGradingPart2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['test/students1.csv', 'test/exercises1.csv', 'test/exam_points1.csv']):
           cls.module = load_module(exercise, 'en')
           

    def test_1_works_with_file_1(self):
        words = ['students1.csv', 'exercises1.csv', 'exam_points1.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program works with input\n{f(words)}")
        
            exp = """pekka peloton 0
jaana javanainen 1
liisa virtanen 3"""
            expRows = exp.split('\n')

            mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")

    def test_2_works_with_file_2(self):
        words = ['students2.csv', 'exercises2.csv', 'exam_points2.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program works with input\n{f(words)}")
        
            exp = """pekka peloton 1
jaana javanainen 1
liisa virtanen 0
donald frump 1
john doe 3
angela tarkel 3
karkki eila 0
alan turing 4
ada lovelace 5"""
            expRows = exp.split('\n')

            mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")

    def test_3_works_with_file_3(self):
        words = ['students3.csv', 'exercises3.csv', 'exam_points3.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program works with input\n{f(words)}")
        
            exp = """pekka peloton 1
jaana javanainen 2
liisa virtanen 3
donald frump 0
john doe 2
angela tarkel 1
karkki eila 1
alan turing 3
ada lovelace 5"""
            expRows = exp.split('\n')

            mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")

    def test_4_works_with_file_4(self):
        words = ['students4.csv', 'exercises4.csv', 'exam_points4.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program works with input\n{f(words)}")
        
            exp = """pekka pelokas 0
mirja virtanen 1
jane doe 3
donald frump 4
john doe 5
kalle paakkola 0
eila kaisla 4
antti tuuri 0
leena lempinen 1
eero honkela 1"""
            expRows = exp.split('\n')

            mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")


   
if __name__ == '__main__':
    unittest.main()
