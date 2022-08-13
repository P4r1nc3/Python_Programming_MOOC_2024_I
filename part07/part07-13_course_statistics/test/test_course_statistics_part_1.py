import unittest
from unittest.mock import patch, MagicMock

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint
import json

exercise = 'src.course_statistics'

class Mok:
    def __init__(self, n):
        self.n = n
        fail = "test/data/courses.json" if n==1 else "test/data/courses2.json"
        with open(fail) as f:
            self.s = f.read()

    def read(self):
        return self.s

@points('7.course_statistics_part1')
class CourseStatisticsPart1Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test0c_request_does_not_use_with_statement(self):
        src_file = os.path.join('src', 'course_statistics.py')
        with open(src_file) as f:
            for line in f:
                if "request.urlopen(" in line and "with" in line :
                    self.assertTrue(False, f"Tests does not work if you call request.urlopen inside with-statement, so following row should be changed \n{line}")

    def test1_function_retrieve_all_exists(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(1)]):
            try:
                from src.course_statistics import retrieve_all
            except:
                self.assertTrue(False, f'Your code should contain function named as retrieve_all()')
            
            try:
                answer = retrieve_all()
            except:
                self.assertTrue(False, f'Make sure, that following function call works retrieve_all()')

            self.assertTrue(type(answer) == list, f'Calling retrieve_all() is expected to return a list, now it returned value {answer}')
            self.assertTrue(len(answer)>0, f'Calling retrieve_all() is expected to return a not empty list, now it returned value {answer}')
            self.assertTrue(type(answer[0]) == tuple, f'The list which function call retrieve_all() returns is expected to contain tuples. Now calling function returned value {answer}')
            self.assertTrue(len(answer[0]) == 4, f'The list which function call retrieve_all() returns is expected to contain tuples which consists of four items. Now calling function returned value {answer}')
            self.assertTrue(type(answer[0][0]) == str, f'The list which function call retrieve_all() returns is expected to contain tuples whose first item is a string. Now calling function returned value {answer}')
            self.assertTrue(type(answer[0][1]) == str, f'The list which function call retrieve_all() returns is expected to contain tuples whose second item is a string. Now calling function returned value {answer}')
            self.assertTrue(type(answer[0][2]) == int, f'The list which function call retrieve_all() returns is expected to contain tuples whose third item is an integer. Now calling function returned value {answer}')
            self.assertTrue(type(answer[0][3]) == int, f'The list which function call retrieve_all() returns is expected to contain tuples whose fourth item is an integer. Now calling function returned value {answer}')

    def test2_function_retrieve_all_works(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(1)]):
            from src.course_statistics import retrieve_all
            answer = retrieve_all()
            expected = [('Full Stack Open 2020', 'ofs2019', 2020, 201), ('DevOps with Docker 2019', 'docker2019', 2019, 36), ('DevOps with Docker 2020', 'docker2020', 2020, 36), ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)]

            self.assertEqual(len(expected), len(answer), f'Calling retrieve_all() is expected to return a list whichs length is {len(expected)}. Now it returned a list whichs length is {len(answer)}. The returned list is\n{answer}')        

            for r in expected:
                self.assertTrue(r in answer, f'The list returned by retrieve_all() should contain tuple {r}. The returned list is\n{answer}')        

            for r in answer:
                self.assertTrue(r in expected, f'The list returned by retrieve_all() should contain tuple {r}. The returned list is\n{answer}')        

    def test3_function_retrieve_all_also_works_with_other_data(self):
        with patch('urllib.request.urlopen', side_effect=[Mok(2)]):
            from src.course_statistics import retrieve_all
            answer = retrieve_all()
            expected = [('Cloud Computing Fundamentals', 'CCFUN', 2019, 27), ('Full Stack Open 2020', 'ofs2019', 2020, 201), ('DevOps with Docker 2018', 'docker2018', 2018, 36), ('DevOps with Docker 2020', 'docker2020', 2020, 54)]

            self.assertEqual(len(expected), len(answer), f'Are you sure, that you did not hard-code the return value? When using an alternative data source, calling retrieve_all() is expected to return a list, whichs length is {len(expected)}. Now it returned a list whichs length is {len(answer)}.  The returned list is\n{answer}')        

            for r in expected:
                self.assertTrue(r in answer, f'Are you sure, that you did not hard-code the return value? When using an alternative data source, the list returned by retrieve_all() is expected to contain tuple {r}.  The returned list is\n{answer}')        

            for r in answer:
                self.assertTrue(r in expected, f'Are you sure, that you did not hard-code the return value? When using an alternative data source, the list returned by retrieve_all() is expected to contain tuple {r}.  The returned list is\n{answer}')        

if __name__ == '__main__':
    unittest.main()