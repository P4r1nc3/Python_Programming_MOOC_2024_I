import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.course_grading_part_4'

def f(d):
    return '\n'.join(d)

datafile1 = 'results.txt'
datafile2 = 'results.csv'

import os
from shutil import copyfile

testdata = ["exam_points1.csv", "exam_points2.csv", "exam_points3.csv", "exam_points4.csv",
"students1.csv", "students2.csv", "students3.csv", "students4.csv", "exercises1.csv", "exercises2.csv", "exercises3.csv", "exercises4.csv",
"course1.txt", "course2.txt", "course3.txt", "course4.txt"]

def get_correct() -> dict:
    pass

def clear_files():
    with open(datafile1, "w"), open(datafile2, "w"):
        pass

def get_content_1():
    with open(datafile1) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

def get_content_2():
    with open(datafile2) as f2:
        return [x.replace("\n","") for x in f2.readlines() if len(x.strip()) > 0]

@points('6.course_grading_part_4')
class CourseGradingPart4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['students1.csv', 'exercises1.csv', 'exam_points1.csv', 'course1.txt']):
            for filename in testdata:
                data_file = os.path.join('src', filename)
                copyfile(data_file, filename)
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_1_works_with_files_1(self):
        words = ['students1.csv', 'exercises1.csv', 'exam_points1.csv', 'course1.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program can be executed with input\n{f(words)}")
        
            exp = """Introduction to Programming, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3"""
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            mssage = """\nPlease note, that in this exercise NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.fail(f"Your program should create file results.txt with imput\n{f(words)}\n{mssage}")  

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"File results.txt is not correct with input\n{f(words)}\nLine:\n{line}\nis not what was exepcted\nIt should be:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"File results.txt is not correct with input\n{f(words)}\nthe file should contain {len(expRows)} lines, but there are {len(txt_file)} lines")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"File results.txt is not correct with input\n{f(words)}\nline\n{line}\nis not what was expected\nThe file should contain the following lines:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Your program should create a file results.csv with input\n{f(words)}")    

        exp = """12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"File results.csv is not correct with input\n{f(words)}\nFile should contain {len(expRows)} lines, now there are {len(csv_file)} lines")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"File results.csv is not correct with input\n{f(words)}\n{f(words)}\nLine\n{line}\nis not what was expected\nTThe file should contain the following lines:\n{exp}")

    def test_2_works_with_files_2(self):
        words = ['students2.csv', 'exercises2.csv', 'exam_points2.csv', 'course2.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that your program can be executed with input\n{f(words)}")
        
            exp = """Advanced Programming Course, 5 credits
======================================
name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
pekka peloton                 25        6         11        17        1         
jaana javanainen              27        6         10        16        1         
liisa virtanen                35        8         6         14        0         
donald frump                  0         0         15        15        1        
john doe                      28        7         16        23        3         
angela tarkel                 32        8         13        21        3         
karkki eila                   30        7         7         14        0         
alan turing                   28        7         19        26        4         
ada lovelace                  17        4         27        31        5   """
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            mssage = """\nPlease note, that in this exercise NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 

            self.fail(f"Your program should create file results.txt with imput\n{f(words)}\n{mssage}")  

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"File results.txt is not correct with input\n{f(words)}\nLine:\n{line}\nis not what was exepcted\nIt should be:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"File results.txt is not correct with input\n{f(words)}\nthe file should contain {len(expRows)} lines, but there are {len(txt_file)} lines")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"File results.txt is not correct with input\n{f(words)}\nline\n{line}\nis not what was expected\nThe file should contain the following lines:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Your program should create a file results.csv with input\n{f(words)}")    

        exp = """12345678;pekka peloton;1
12345687;jaana javanainen;1
12345699;liisa virtanen;0
12345688;donald frump;1
12345698;john doe;3
12345700;angela tarkel;3
12345701;karkki eila;0
12345702;alan turing;4
12345704;ada lovelace;5"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"File results.csv is not correct with input\n{f(words)}\nFile should contain {len(expRows)} lines, now there are {len(csv_file)} lines")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"File results.csv is not correct with input\n{f(words)}\n{f(words)}\nLine\n{line}\nis not what was expected\nTThe file should contain the following lines:\n{exp}")


   
if __name__ == '__main__':
    unittest.main()
