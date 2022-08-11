import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.course_grading_part_3'

def f(d):
    return '\n'.join(d)

def w(x):
    return [f"test/{i}" for i in x]

@points('6.course_grading_part_3')
class CourseGradingPart3Test(unittest.TestCase):
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
                self.assertTrue(False, f"Ensure that your program can be executed with input\n{f(words)}")
        
            exp = """name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3"""
            expRows = exp.split('\n')

            mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block"""
            #\n{mssage}") 
            self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
            self.assertEqual(output[0], expRows[0], f"Your program does not work correctly with input\n{f(words)}\nThe first output line should be\n{expRows[0]}\nNow it is\n{output[0]}\nWhole output is:\n{output_all}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")

    
    def test_2_works_with_file_3(self):
            words = ['students3.csv', 'exercises3.csv', 'exam_points3.csv']
            with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Ensure that your program can be executed with input\n{f(words)}")
            
                exp = """name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 25        6         9         15        1
jaana javanainen              30        7         11        18        2
liisa virtanen                34        8         14        22        3
donald frump                  40        10        0         10        0
john doe                      36        9         10        19        2
angela tarkel                 16        4         13        17        1
karkki eila                   26        6         10        16        1
alan turing                   24        6         17        23        3
ada lovelace                  26        6         24        30        5"""
                expRows = exp.split('\n')

                mssage = """\nPlease note, that in this program NO CODE should be included inside
    if __name__ == "__main__":
    block"""
                #\n{mssage}") 
                self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
                self.assertEqual(output[0], expRows[0], f"Your program does not work correctly with input\n{f(words)}\nThe first output line should be\n{expRows[0]}\nNow it is\n{output[0]}\nWhole output is:\n{output_all}")
                for i in range(len(expRows)):
                    line = output[i]
                    self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")

    def test_3_works_with_file_4(self):
            words = ['students4.csv', 'exercises4.csv', 'exam_points4.csv']
            with patch('builtins.input', side_effect =w(words) + [ AssertionError("Too many inputs.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Ensure that your program can be executed with input\n{f(words)}")
            
                exp = """name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka pelokas                 25        6         6         12        0
mirja virtanen                30        7         8         15        1
jane doe                      33        8         14        22        3
donald frump                  35        8         16        24        4
john doe                      36        9         20        29        5
kalle paakkola                16        4         9         13        0
eila kaisla                   29        7         19        26        4
antti tuuri                   18        4         8         12        0
leena lempinen                26        6         10        16        1
eero honkela                  21        5         11        16        1"""
                expRows = exp.split('\n')

                mssage = """\nPlease note, that in this program NO CODE should be included inside
    if __name__ == "__main__":
    block"""
                #\n{mssage}") 
                self.assertTrue(len(output_all)>0, f"Your program does not output anything with input\n{f(words)}\n{mssage}") 
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expRows), len(output), f"Instead of {len(expRows)} rows, your program outputs {len(output)} rows:\n{output_all}\nwith input:\n{f(words)}\nOutput should contain the following lines:\n{exp}")
                self.assertEqual(output[0], expRows[0], f"Your program does not work correctly with input\n{f(words)}\nThe first output line should be\n{expRows[0]}\nNow it is\n{output[0]}\nWhole output is:\n{output_all}")
                for i in range(len(expRows)):
                    line = output[i]
                    self.assertTrue(line.strip() in exp, f"Your program does not work correctly with input\n{f(words)}\nLine {line} is not what expected\nOutput should contain the following lines:\n{exp}\nThe whole output is:\n{output_all}")


if __name__ == '__main__':
    unittest.main()
