import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.student_database'
function1 = 'add_student'
function2 = 'print_student'
function3 = 'add_course'

@points('5.student_database_part2')
class StudentDatabasePart2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_part2_1_function_exists(self):
        try:
            from src.student_database import add_course
        except:
            self.assertTrue(False, f'Your code should conorn function named as {function3}(students: dict, name: str, completion: tuple)')

        try:
            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            students = {}
            add_student(students, "Peter")
            add_course(students, "Peter", ("Introduction to Programming", 5))
        except:
            code = """students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 5))"""
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code:{code}')

    def test_part2_2_completion_is_printed_out(self):

        output_at_start = get_stdout()
        try:
            code = """students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 5))
print_student(students, "Peter")"""

            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Peter")
            add_course(students, "Peter", ("Introduction to Programming", 5))

            print_student(students, "Peter")

            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """Peter:
 1 completed courses:
  Introduction to Programming 5
 average grade 5.0"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is\n{output[i]}" )

    def test_part2_3_completions_are_printed_out(self):

        output_alussa = get_stdout()
        try:
            code = """students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 5))
add_course(students, "Peter", ("Data Structures and Algorithms", 3))
print_student(students, "Peter")"""

            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Peter")
            add_course(students, "Peter", ("Introduction to Programming", 5))
            add_course(students, "Peter", ("Data Structures and Algorithms", 3))

            print_student(students, "Peter")

            output_all = get_stdout().replace(output_alussa, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]


            expr1 = """Peter:
 2 completed courses:
  Introduction to Programming 5
  Data Structures and Algorithms 3
 average grade 4.0"""

            expr2 = """Peter:
 2 completed courses:
  Data Structures and Algorithms 3
  Introduction to Programming 5
 average grade 4.0"""
            exp1 = expr1.split('\n')
            exp2 = expr2.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp1)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp1), f"Your program is expected to print out {len(exp1)} rows when executing the following code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp1)):
            if exp1[i] == exp2[i]:
                self.assertTrue(output[i].rstrip() ==  exp1[i] or output[i].rstrip() ==  exp2[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp1[i]}\nbut it is\n{output[i]}" )
            else:
                self.assertTrue(output[i].rstrip() ==  exp1[i] or output[i].rstrip() ==  exp2[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp1[i]}\nor\n{exp2[i]}\nbut it is\n{output[i]}" )
    
    def test_part2_4_completions_are_printed_out(self):

        output_at_start = get_stdout()
        try:

            code = """students = {}
add_student(students, "Emily")
add_student(students, "Peter")
add_course(students, "Emily", ("Introduction to Programming", 5))
add_course(students, "Emily", ("Introduction to Databases", 4))
add_course(students, "Peter", ("Data Structures and Algorithms", 3))
print_student(students, "Emily")"""

            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Emily")
            add_student(students, "Peter")
            add_course(students, "Emily", ("Introduction to Programming", 5))
            add_course(students, "Emily", ("Introduction to Databases", 4))
            add_course(students, "Peter", ("Data Structures and Algorithms", 3))

            print_student(students, "Emily")

            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr1 = """Emily:
 2 completed courses:
  Introduction to Programming 5
  Introduction to Databases 4
 average grade 4.5"""

            expr2 = """Emily:
 2 completed courses:
 Introduction to Databases 4
  Introduction to Programming 5
 average grade 4.5"""

            exp1 = expr1.split('\n')
            exp2 = expr2.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp1)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp1), f"Your program is expected to print out {len(exp1)} rows when executing the following code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp1)):
            self.assertTrue(output[i].rstrip() ==  exp1[i] or output[i].rstrip() ==  exp2[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp1[i]}\nor\n{exp2[i]}\nbut it is\n{output[i]}" )


if __name__ == '__main__':
    unittest.main()
