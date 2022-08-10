import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.phone_book_v2'

def f(d):
    return '\n'.join(d)
def s(d):
    return d.split('\n')

@points('5.phone_book_v2')
class PhoneBookV2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["3"]):
            cls.module = load_module(exercise, 'en')

    def test_1_program_stops(self):

        with patch('builtins.input', side_effect = ["3", AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n3")
    
    def test_2_not_added_is_not_found(self):
        test_input="""1
mary
3"""
        words = s(test_input)
        with patch('builtins.input', side_effect = s(test_input) + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
        
            exp = """no number
quitting..."""

            expWordrs = exp.split('\n')

            mssage = """\nPlease note, that in this exercise, no code should be included inside
if __name__ == "__main__":
block
            """
            #\n{mssage}") 
            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs), len(output), f"Instead of {len(expWordrs)} rows, your program prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nexpected print out is\n{exp}")
            for i in range(len(expWordrs)):
                e = expWordrs[i]
                line = output[i]
                self.assertEqual(line, e, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nbut it is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp}")

    def test_3_added_is_found(self):
        test_input="""2
mary
040-234567
1
mary
3"""
        words = s(test_input)
        with patch('builtins.input', side_effect = s(test_input) + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
        
            exp = """ok!
040-234567
quitting..."""

            expWordrs = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs), len(output), f"Instead of {len(expWordrs)} rows, your program prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nexpected print out is\n{exp}")
            for i in range(len(expWordrs)):
                e = expWordrs[i]
                line = output[i]
                self.assertEqual(line, e, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nbut it is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp}")

    def test_4_new_number_is_added(self):
        test_input="""2
mary
040-234567
2
mary
09-334455
1
mary
3"""
        words = s(test_input)
        with patch('builtins.input', side_effect = s(test_input) + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
        
            exp1 = """ok!
ok!
040-234567
09-334455
quitting..."""

            exp2 = """ok!
ok!
09-334455
040-234567
quitting..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                                                            # f"Instead of {len(expWordrs)} rows, your program prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nexpected print out is\n{exp}"
            self.assertEqual(len(expWordrs1), len(output), f"Instead of {len(expWordrs1)} rows, your programs prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nRemember, that in this exercise new number should not replace the old number!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nbut it is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nor\n{e}\nbut the row is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")

    def test_5_many_commands(self):
        test_input="""2
mike
040-234567
2
mary
09-334455
1
mary
1
mike
1
becky
2
mike
045-554433
1
mike
3"""
        words = s(test_input)
        with patch('builtins.input', side_effect = s(test_input) + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
        
            exp1 = """ok!
ok!
09-334455
040-234567
no number
ok!
045-554433
040-234567
quitting..."""
        
            exp2 = """ok!
ok!
09-334455
040-234567
no number
ok!
040-234567
045-554433
quitting..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs1), len(output), f"Instead of {len(expWordrs1)} rows, your programs prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nRemember, that in this exercise new number should not replace the old number!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nbut it is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nor\n{e}\nbut the row is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")

    def test_6_many_commands(self):
        test_input="""2
jack
040-1212334
2
wendy
09-334455
2
william
050-2255433
1
mary
1
wendy
1
william
2
jack
045-554433
1
jack
3"""
        words = s(test_input)
        with patch('builtins.input', side_effect = s(test_input) + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
        
            exp1 = """ok!
ok!
ok!
no number
09-334455
050-2255433
ok!
040-1212334
045-554433
quitting..."""

            exp2 = """ok!
ok!
ok!
no number
09-334455
050-2255433
ok!
045-554433
040-1212334
quitting..."""

            expWordrs1 = exp1.split('\n')
            expWordrs2 = exp2.split('\n')

            self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expWordrs1), len(output), f"Instead of {len(expWordrs1)} rows, your programs prints out {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}\nRemember, that in this exercise new number should not replace the old number!")
            for i in range(len(expWordrs1)):
                e = expWordrs1[i]
                e2 = expWordrs2[i]
                line = output[i]
                if expWordrs1[i] == expWordrs2[i]:
                    self.assertEqual(line, e, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nbut it is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")
                else:
                    self.assertTrue(line==e or line==e2, f"Your program is not working correctly with the input\n{f(words)}\nprint out on row {i+1} is incorrect, it should be\n{e}\nor\n{e}\nbut the row is\n{line}\nThe whole print out is:\n{output_all}\nThe expected print out is\n{exp1}")

if __name__ == '__main__':
    unittest.main()