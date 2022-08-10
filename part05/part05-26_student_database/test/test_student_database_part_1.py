import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.student_database'
function1 = 'add_student'
function2 = 'print_student'

@points('5.student_database_part1')
class StudentDatabasePart1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_part1_1_function_exists(self):
        try:
            from src.student_database import add_student
        except:
            self.assertTrue(False, f'Your code should contain function named as {function1}(students: dict, name: str)')
        try:
            add_student = load(exercise, function1, 'en')
            add_student({}, "Peter")
        except:
            code = """students = {}
add_student(students, "Peter")"""
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code: \n{code}')

    def test_part1_2_function_exists(self):
        try:
            from src.student_database import print_student
        except:
            self.assertTrue(False, f'Your code should contain function named as {function2}(students: dict, name: str)')
        try:
            print_student = load(exercise, function2, 'en')
            code = """students = {}
print_student(students, "Peter")"""
            print_student({}, "Peter")
        except:
            self.assertTrue(False, f'Make sure, that the function can be called as in the following code: {code}')


    def test_part1_3_added_is_in_print_out(self):

        output_at_start = get_stdout()
        try:

            code = """students = {}
add_student(students, "Peter")
print_student(students, "Peter")"""

            add_student = load(exercise, function1, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Peter")
            print_student(students, "Peter")
            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """Peter:
 no completed courses"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works:\n{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is ecpected to print out {len(exp)} rows when executing the follwing code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is:\n{output[i]}" )

    def test_part1_4_printing_student_not_added(self):

        output_at_start = get_stdout()
        try:
            add_student = load(exercise, function1, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Peter")
            print_student(students, "Emily")
            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            code = """students = {}
add_student(students, "Peter")
print_student(students, "Emily")"""

            expr = """Emily: no such person in the database"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works:\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is ecpected to print out {len(exp)} rows when executing the follwing code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is:\n{output[i]}" )

    def test_osa1_5_many_print_student_function_calls(self):

        code = """students = {}
add_student(students, "Peter")
add_student(students, "Emily")
print_student(students, "Peter")
print_student(students, "Emily")
print_student(students, "Andy")
"""

        output_at_start = get_stdout()
        try:
            add_student = load(exercise, function1, 'en')
            print_student = load(exercise, function2, 'en')
            students = {}
            add_student(students, "Peter")
            add_student(students, "Emily")
            print_student(students, "Peter")
            print_student(students, "Emily")
            print_student(students, "Andy")
            output_all = get_stdout().replace(output_at_start, '', 1)
            output = [l for l in output_all.split("\n") if len(l)>0 ]

            expr = """Peter:
 no completed courses
Emily:
 no completed courses
Andy: no such person in the database"""
            exp = expr.split('\n')

        except:
            self.assertTrue(False, f"Make sure, the execution of the following code works:\n\{code}" )

        self.assertFalse(len(output_all) == 0, f"Your program is expected to print out {len(exp)} rows when executing the following code:\n{code}\nNow it does not print out anything" )
        self.assertEqual(len(output), len(exp), f"Your program is ecpected to print out {len(exp)} rows when executing the follwing code:\n{code}\nNow it prints out {len(output)} rows:\n{output_all}" )
        for i in range(len(exp)):
            self.assertEqual(output[i].rstrip(), exp[i], f"When executing the following code:\n{code}\nThe row number {i+1} should be:\n{exp[i]}\nbut it is:\n{output[i]}" )


if __name__ == '__main__':
    unittest.main()