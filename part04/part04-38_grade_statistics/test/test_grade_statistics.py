import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.grade_statistics'

def f(d):
    return '\n'.join(d)
 
@points('4.grade_statistics')
class GradeStatisticsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["20 100", "12 34",""]):
            cls.module = load_module(exercise, 'en')

    def test_program_stops(self):
        words = "20 100;".split(";")
    
        with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")
    
    def test_functionality_1(self):
            words = "20 100;".split(";")         
            expected = """Statistics:
Points average: 30.0
Pass percentage: 100.0
Grade distribution:
  5: *
  4:
  3:
  2:
  1:
  0:""".split('\n')
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")

                mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
                #\n{mssage}") 

                self.assertTrue(len(output_all)>0, f"Your program does not printout anything with the input\n{f(words)}\n{mssage}") 
                output = [line for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expected), len(output), f"Instead of 10 rows, your program output is now in {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}")   
                for i in range(len(expected)):
                    e = expected[i].strip()
                    line = output[i].strip()
                    self.assertEqual(line, e, f"The print out in row {i+1} is incorrect, it should be\n{e}\nbut row is\n{line}\nthe whole print out is:\n{output_all}\nwith the input:\n{f(words)}")

    def test_functionality_2(self):
            words = "9 100;".split(";")         
            expected = """Statistics:
Points average: 19.0
Pass percentage: 0.0
Grade distribution:
  5:
  4:
  3:
  2:
  1:
  0: *""".split('\n')
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Make sure, that the program stops with the input\n{f(words)}")

                self.assertTrue(len(output_all)>0, f"Your program does not printout anything with the input\n{f(words)}")   
                output = [line for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(expected), len(output), f"Instead of 10 rows, your program output is now in {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}")   
                for i in range(len(expected)):
                    e = expected[i].strip()
                    line = output[i].strip()
                    self.assertEqual(line, e, f"The print out in row {i+1} is incorrect, it should be\n{e}\nbut row is\n{line}\nthe whole print out is:\n{output_all}\nwith the input:\n{f(words)}")

if __name__ == '__main__':
    unittest.main()