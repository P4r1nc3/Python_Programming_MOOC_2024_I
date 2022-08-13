import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.screen_time'

def f(a):
    return "\n".join(a)

def get_content(tiedosto):
    try:
        with open(tiedosto) as f:
            return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]
    except:
        return None

@points('7.screen_time')
class ScreenTimeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["first_of_may.txt", "1.5.2020", "1", "30 0 5"]):
           cls.module = load_module(exercise, 'en')
    
    def test_functionality_1(self):
        inpt = ["first_of_may.txt", "1.5.2020", "1", "30 0 5"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following inputs:\n{f(inpt)}")

            output = get_stdout()
            

            msg = 'Note, that in this program no code must not be placed inside the if __name__ == "main" -block.'

            file_name = inpt[0]
            try:
                content = get_content(file_name)
                if not content:
                    self.assertTrue(False, msg)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write a report to a file named {file_name}")

            correct = """Time period: 01.05.2020-01.05.2020
Total minutes: 35
Average minutes: 35.0
01.05.2020: 30/0/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")

    def test_functionality_2(self):
        inpt = ["early_june.txt", "1.6.2020", "3", "30 0 5", "180 90 15", "0 240 25"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following input:\n{f(inpt)}")

            output = get_stdout()
            file_name = inpt[0]
            try:
                content = get_content(file_name)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write report to a file named {file_name}")

            correct = """Time period: 01.06.2020-03.06.2020
Total minutes: 585
Average minutes: 195.0
01.06.2020: 30/0/5
02.06.2020: 180/90/15
03.06.2020: 0/240/25"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")

    def test_functionality_3(self):
        inpt = ["late_june.txt", "29.6.2020", "4", "30 100 0", "55 40 0", "0 240 25", "180 240 100"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following input:\n{f(inpt)}")

            output = get_stdout()
            file_name = inpt[0]
            try:
                content = get_content(file_name)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write report to a file named {file_name}")

            correct = """Time period: 29.06.2020-02.07.2020
Total minutes: 1010
Average minutes: 252.5
29.06.2020: 30/100/0
30.06.2020: 55/40/0
01.07.2020: 0/240/25
02.07.2020: 180/240/100"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")

    def test_functionality_4(self):
        inpt = ["late_february.txt", "27.2.2020", "5", "30 15 15", "20 140 100", "10 200 35", "0 0 300", "5 5 5"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following input:\n{f(inpt)}")

            output = get_stdout()
            
            file_name = inpt[0]
            try:
                content = get_content(file_name)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write report to a file named {file_name}")

            correct = """Time period: 27.02.2020-02.03.2020
Total minutes: 880
Average minutes: 176.0
27.02.2020: 30/15/15
28.02.2020: 20/140/100
29.02.2020: 10/200/35
01.03.2020: 0/0/300
02.03.2020: 5/5/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")

    def test_functionality_5(self):
        inpt = ["late_february_2021.txt", "27.2.2021", "5", "30 15 15", "20 140 100", "10 200 35", "0 0 300", "5 5 5"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following input:\n{f(inpt)}")

            output = get_stdout()
            file_name = inpt[0]
            try:
                content = get_content(file_name)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write report to a file named {file_name}")

            correct = """Time period: 27.02.2021-03.03.2021
Total minutes: 880
Average minutes: 176.0
27.02.2021: 30/15/15
28.02.2021: 20/140/100
01.03.2021: 10/200/35
02.03.2021: 0/0/300
03.03.2021: 5/5/5"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")
    
    def test_functionality_6(self):
        inpt = ["turn_of_the_year.txt", "29.12.2020", "6", "30 15 15", "5 140 90", "0 100 35", "5 15 15",  "0 0 0",  "100 10 10"]
        with patch('builtins.input', side_effect=inpt):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works with the following input:\n{f(inpt)}")

            output = get_stdout()
            
            file_name = inpt[0]
            try:
                content = get_content(file_name)
            except:
                self.assertTrue(False, f"With the input:\n{f(inpt)}\nyour program should write report to a file named {file_name}")

            correct = """Time period: 29.12.2020-03.01.2021
Total minutes: 585
Average minutes: 97.5
29.12.2020: 30/15/15
30.12.2020: 5/140/90
31.12.2020: 0/100/35
01.01.2021: 5/15/15
02.01.2021: 0/0/0
03.01.2021: 100/10/10"""
            cLines = correct.split('\n')

            self.assertEqual(len(content), len(cLines), f"When the program is executed with the following input:\n{f(inpt)}\nFile {file_name} is expected to contain {len(cLines)} rows, but file contains {len(content)} rows\nWhole content of the file is:\n{f(content)}")

            for i in range(0, len(cLines)):
                r = content[i].strip()
                c = cLines[i].strip()
                self.assertEqual(r, c, f"When the program is executed with the following input:\n{f(inpt)}\nIn file {file_name} row number {i+1} is expected to be\n{c}\nbut it:\n{r}\nWhole content of the file is:\n{f(content)}")


if __name__ == '__main__':
    unittest.main()
