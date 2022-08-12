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

class MokCourse:
    def __init__(self, n):
        with open(f"test/data/{n}.json" ) as f:
            self.s = f.read()

    def read(self):
        return self.s

@points('7.course_statistics_part2')
class CourseStatisticsPart2Test(unittest.TestCase):

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

    def test1_function_retrieve_course_exists(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("docker2019")]):
            try:
                from src.course_statistics import retrieve_course
            except:
                self.assertTrue(False, f'Your code should contain function named as retrieve_course(course_name: str)')
            
            try:
                answer = retrieve_course("docker2019")
            except:
                self.assertTrue(False, f'Make sure, that following function call works retrieve_course("docker2019")')

            self.assertTrue(type(answer) == dict, f'Function retrieve_course("docker2019") is expected to return a value whics type is dict, now it returned value {answer}')

    def test2_function_retrieve_course_works_1(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("docker2019")]):
            from src.course_statistics import retrieve_course
            
            code = 'retrieve_course("docker2019")'
            expected = {'weeks': 4, 'students': 220, 'hours': 5966, 'hours_average': 27, 'exercises': 4988, 'exercises_average': 22}
            try:
                answer = retrieve_course("docker2019")
            except:
                self.assertEqual(expected.keys(), answer.keys(), f'Calling {code} results to an error')        

            self.assertEqual(expected.keys(), answer.keys(), f'Calling {code}, is expected to return a dictionary which contains following keys {expected.keys()}.\nFunction returns{answer}')        

            for k, v in expected.items():
                self.assertEqual(answer[k], v, f'Calling {code} is expected return a dictionary which contains a key {k} that has a value {v}, but the value of the key is {answer[k]}\nFunction returns{answer}')        

    def test2_function_retrieve_course_works_2(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("CCFUN")]):
            from src.course_statistics import retrieve_course
            
            expected = {'weeks': 9, 'students': 59, 'hours': 1687, 'hours_average': 28, 'exercises': 951, 'exercises_average': 16}
            code = 'retrieve_course("CCFUN")'

            try:
                answer = retrieve_course("CCFUN")
            except:
                self.assertFalse(True, f'Calling {code} results to an error')    

            self.assertEqual(expected.keys(), answer.keys(), f'Calling {code}, is expected to return a dictionary which contains following keys {expected.keys()}.\nFunction returns{answer}')        

            for k, v in expected.items():
                self.assertEqual(answer[k], v, f'Calling {code} is expected return a dictionary which contains a key {k} that has a value {v}, but the value of the key is {answer[k]}\nFunction returns{answer}')        

    def test2_function_retrieve_course_works_3(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ohtus17")]):
            from src.course_statistics import retrieve_course
            
            expected = {'weeks': 7, 'students': 96, 'hours': 2977, 'hours_average': 31, 'exercises': 5381, 'exercises_average': 56}
            code = 'retrieve_course("ohtus17")'

            try:
                answer = retrieve_course("ohtus17")
            except:
                self.assertFalse(True, f'Calling {code} results to an error')    

            self.assertEqual(expected.keys(), answer.keys(), f'Calling {code}, is expected to return a dictionary which contains following keys {expected.keys()}.\nFunction returns{answer}')        

            for k, v in expected.items():
                self.assertEqual(answer[k], v, f'Calling {code} is expected return a dictionary which contains a key {k} that has a value {v}, but the value of the key is {answer[k]}\nFunction returns{answer}')        

    def test2_function_retrieve_course_works_4(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ofs")]):
            from src.course_statistics import retrieve_course
           
            expected = {'weeks': 9, 'students': 542, 'hours': 28116, 'hours_average': 51, 'exercises': 31746, 'exercises_average': 58}
            code = 'retrieve_course("ofs")'
            try:
                 answer = retrieve_course("ofs")
            except:
                self.assertFalse(True, f'Calling {code} results to an error')    

            self.assertEqual(expected.keys(), answer.keys(), f'Calling {code}, is expected to return a dictionary which contains following keys {expected.keys()}.\nFunction returns{answer}')        

            for k, v in expected.items():
                self.assertEqual(answer[k], v, f'Calling {code} is expected return a dictionary which contains a key {k} that has a value {v}, but the value of the key is {answer[k]}\nFunction returns{answer}')        

    def test2_function_retrieve_course_works_5(self):
        with patch('urllib.request.urlopen', side_effect=[MokCourse("ofs2019")]):
            from src.course_statistics import retrieve_course
            
            expected = {'weeks': 11, 'students': 4441, 'hours': 201752, 'hours_average': 45, 'exercises': 238712, 'exercises_average': 53}
            code = 'retrieve_course("ofs2019")'
            try:
                 answer = retrieve_course("ofs2019")
            except:
                self.assertFalse(True, f'Calling {code} results to an error')   

            self.assertEqual(expected.keys(), answer.keys(), f'Calling {code}, is expected to return a dictionary which contains following keys {expected.keys()}.\nFunction returns{answer}')        

            for k, v in expected.items():
                self.assertEqual(answer[k], v, f'Calling {code} is expected return a dictionary which contains a key {k} that has a value {v}, but the value of the key is {answer[k]}\nFunction returns{answer}')        

if __name__ == '__main__':
    unittest.main()