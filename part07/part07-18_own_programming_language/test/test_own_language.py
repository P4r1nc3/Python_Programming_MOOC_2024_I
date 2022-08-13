import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.own_language'
function = "run"

class OwnLanguageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testng the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    @points('7.own_programming_language-part1')
    def test1_function_exists(self):
        try:
            from src.own_language import run
        except:
            self.assertTrue(False, "Your program should contain function named as run")

    @points('7.own_programming_language-part1')
    def test2_no_loop(self):
        tests = []
        program1 = ["PRINT A","END"]
        result1 = [0]
        tests.append((program1,result1))
        program2 = ["MOV A 5","PRINT A"]
        result2 = [5]
        tests.append((program2,result2))
        program3 = ["MOV A 1","MOV B 1","ADD A B","ADD B A","ADD A B","ADD B A","PRINT A","PRINT B"]
        result3 = [5,8]
        tests.append((program3,result3))
        program4 = ["MOV A 2","MUL A A","MUL A A","MUL A A","MUL A A","PRINT A"]
        result4 = [65536]
        tests.append((program4,result4))
        program5 = ["MOV A 10","PRINT A","MOV B A","SUB B 8","PRINT B","SUB A B","PRINT A"]
        result5 = [10,2,8]
        tests.append((program5,result5))
        for test in tests:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                run = load(exercise, function, 'en')
                try:
                    result = run(test[0])
                except:
                    self.assertFalse(True, "Program "+str(test[0])+" caused an error")
                self.assertEqual(result, test[1], "Program "+str(test[0])+" returns an incorrect result "+str(result)+", the correct result would be "+str(test[1]))

    @points('7.own_programming_language-part2')
    def test3_all_commands(self):
        tests = []
        program1 = ["PRINT A","END"]
        result1 = [0]
        tests.append((program1,result1))
        program2 = []
        result2 = []
        tests.append((program2,result2))
        program3 = ["MOV A 10","start:","PRINT A","SUB A 1","IF A > 0 JUMP start","END"]
        result3 = [10,9,8,7,6,5,4,3,2,1]
        tests.append((program3,result3))
        program4 = ["MOV A 1","MOV B 1","start:","MUL A 2","ADD B 1","IF B != 101 JUMP start","PRINT A"]
        result4 = [1267650600228229401496703205376]
        tests.append((program4,result4))
        program5 = ["MOV A 1","MOV B 999","start:","ADD A 1","SUB B 1","ADD C 1","IF A == B JUMP end","JUMP start","end:","PRINT C"]
        result5 = [499]
        tests.append((program5,result5))
        program6 = ["MOV N 100","PRINT 2","MOV A 3","start:","MOV B 2","MOV Z 0","test:","MOV C B","new:","IF C == A JUMP virhe","IF C > A JUMP pass_by","ADD C B","JUMP new","virhe:","MOV Z 1","JUMP pass_by2","pass_by:","ADD B 1","IF B < A JUMP test","pass_by2:","IF Z == 1 JUMP pass_by3","PRINT A","pass_by3:","ADD A 1","IF A <= N JUMP start"]
        result6 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        tests.append((program6,result6))
        for test in tests:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                run = load(exercise, function, 'en')
                try:
                    result = run(test[0])
                except:
                    self.assertFalse(True, "Program "+str(test[0])+" causes on error")
                self.assertEqual(result, test[1], "Program "+str(test[0])+" returns an incorrect result "+str(result)+", the correct result would be "+str(test[1]))

if __name__ == '__main__':
    unittest.main()