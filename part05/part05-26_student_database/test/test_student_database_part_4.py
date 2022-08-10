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
function4 = 'summary'

@points('5.student_database_part4')
class StudentDatabasePart4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_part4_1_function_exists(self):
        try:
            from src.student_database import summary
        except:
            self.assertTrue(False, f'Your code should contain function named as {function4}(students: dict)')
       
        try:
            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            summary = load(exercise, function4, 'en')

            students = {}
            add_student(students, "Peter")
            add_course(students, "Peter", ("Software Development Methods", 5))
            summary(students)
        except:
            code = """students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Software Development Methods", 5))
summary(students)"""
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code:\n{code}')

    def test_part4_2_print_out_is_correct(self):
        output_at_start = get_stdout()
        try:
            code = """students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Software Development Methods", 5))
summary(students)"""            
            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            summary = load(exercise, function4, 'en')
            print_student = load(exercise, function2, 'en')

            students = {}
            add_student(students, "Peter")
            add_course(students, "Peter", ("Software Development Methods", 5))
            summary(students)

            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """students 1
most courses completed 1 Peter
best average grade 5.0 Peter"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is:\n{output[i]}" )


    def test_part4_3_print_out_is_correct(self):
        output_at_start = get_stdout()
        try:

            code = """students = {}
add_student(students, "Emily")
add_student(students, "Peter")
add_course(students, "Emily", ("Software Development Methods", 4))
add_course(students, "Emily", ("Software Development Methods", 5))
add_course(students, "Peter", ("Data Structures and Algorithms", 3))
add_course(students, "Peter", ("Models of Computation", 0))
add_course(students, "Peter", ("Data Structures and Algorithms", 2))
add_course(students, "Peter", ("Introduction to Computer Science", 1))
add_course(students, "Peter", ("Software Engineering", 3))
summary(students)
summary(students)"""


            add_student = load(exercise, function1, 'en')
            add_course = load(exercise, function3, 'en')
            summary = load(exercise, function4, 'en')
            print_student = load(exercise, function2, 'en')

            students = {}
            add_student(students, "Emily")
            add_student(students, "Peter")
            add_course(students, "Emily", ("Software Development Methods", 4))
            add_course(students, "Emily", ("Software Development Methods", 5))
            add_course(students, "Peter", ("Data Structures and Algorithms", 3))
            add_course(students, "Peter", ("Models of Computation", 0))
            add_course(students, "Peter", ("Data Structures and Algorithms", 2))
            add_course(students, "Peter", ("Introduction to Computer Science", 1))
            add_course(students, "Peter", ("Software Engineering", 3))
            summary(students)

            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """students 2
most courses completed 3 Peter
best average grade 5.0 Emily"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is:\n{output[i]}" )


if __name__ == '__main__':
    unittest.main()
