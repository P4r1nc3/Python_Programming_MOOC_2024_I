import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.json_files'

import os
from shutil import copyfile

testdata = ['file1.json', 'file2.json', 'file3.json', 'file4.json']

def f(p):
    return "\n".join(p)

@points('7.json_files')
class JsonFilesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)      
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test1_function_exists(self):
        try:
             from src.json_files import print_persons
        except:
            self.assertTrue(False, f'Your code should conrtain function named as print_persons(filename: str)')
        
        try:  
            print_persons("file1.json")
        except:
            self.assertTrue(False, f'Make sure, that following function call works print_persons("file1.json")')

    def test_2_works_with_file1(self):
        from src.json_files import print_persons
        output_at_start = get_stdout()
        print_persons("file1.json")
        code = 'print_persons("file1.json")'
        output_all = get_stdout().replace(output_at_start, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Peter Pythons 27 years (coding, knitting)
Jean Javanese 24 years (coding, rock climbing, reading)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'When executing the following code {code}, your program does not print out anything.')
        self.assertEqual(len(cLines),len(output), f'When executing the following code {code}, the print out is expected to be in {len(cLines)} rows. The print out contained {len(output)} rows:\n{f(output)}')
        for row in cLines:
            self.assertTrue(row in output, f'When executing the following code {code}, the print out is expected to contain row\n{row}\nWhole print out of the program was\n{f(output)}')
        for row in output:
            self.assertTrue(row in correct, f'When executing the following code {code}, following row was in the print out\n{row}\nThe correct print out contains only following rows\n{f(correct)}')

    def test_2_works_with_file2(self):
        from src.json_files import print_persons
        output_at_start = get_stdout()
        print_persons("file2.json")
        code = 'print_persons("file2.json")'
        output_all = get_stdout().replace(output_at_start, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Alf Newlyinventend 42 years (karate)
Frances Fictious 52 years (running, martial arts)
Emily Paulson 4 years (puzzles)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'When executing the following code {code}, your program does not print out anything.')
        self.assertEqual(len(cLines),len(output), f'When executing the following code {code}, the print out is expected to be in {len(cLines)} rows. The print out contained {len(output)} rows:\n{f(output)}')
        for row in cLines:
            self.assertTrue(row in output, f'When executing the following code {code}, the print out is expected to contain row\n{row}\nWhole print out of the program was\n{f(output)}')
        for row in output:
            self.assertTrue(row in correct, f'When executing the following code {code}, following row was in the print out\n{row}\nThe correct print out contains only following rows\n{f(correct)}')

    def test_2_works_with_file3(self):
        from src.json_files import print_persons
        output_at_start = get_stdout()
        print_persons("file3.json")
        code = 'print_persons("file3.json")'
        output_all = get_stdout().replace(output_at_start, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Emerson Lawson 78 years (reading, running)
Sammy Evans 32 years (algorithms, playing violin)
Bev Holmes 8 years (parkour, basket ball)
Logan Gray 8 years (football, airplanes)
Gabe Webb 46 years (programming, spectator sports)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'When executing the following code {code}, your program does not print out anything.')
        self.assertEqual(len(cLines),len(output), f'When executing the following code {code}, the print out is expected to be in {len(cLines)} rows. The print out contained {len(output)} rows:\n{f(output)}')
        for row in cLines:
            self.assertTrue(row in output, f'When executing the following code {code}, the print out is expected to contain row\n{row}\nWhole print out of the program was\n{f(output)}')
        for row in output:
            self.assertTrue(row in correct, f'When executing the following code {code}, following row was in the print out\n{row}\nThe correct print out contains only following rows\n{f(correct)}')

    def test_2_works_with_file4(self):
        from src.json_files import print_persons
        output_at_start = get_stdout()
        print_persons("file4.json")
        code = 'print_persons("file4.json")'
        output_all = get_stdout().replace(output_at_start, '', 1)
        output = [l for l in output_all.split("\n") if len(l)>0 ]
        
        correct = """Jane Doe 100 years ()
Sanna Marin 38 years (history, politics)
Janja Garnbret 21 years (bouldering, rock climbing)
Adam Ondra 28 years (bouldering, rock climbing)
Barack Obama 62 years (politics, music)
Elisabeth Rehn 78 years (national defense, music)"""

        cLines = correct.split('\n')
        self.assertTrue(len(output_all)>0, f'When executing the following code {code}, your program does not print out anything.')
        self.assertEqual(len(cLines),len(output), f'When executing the following code {code}, the print out is expected to be in {len(cLines)} rows. The print out contained {len(output)} rows:\n{f(output)}')
        for row in cLines:
            self.assertTrue(row in output, f'When executing the following code {code}, the print out is expected to contain row\n{row}\nWhole print out of the program was\n{f(output)}')
        for row in output:
            self.assertTrue(row in correct, f'When executing the following code {code}, following row was in the print out\n{row}\nThe correct print out contains only following rows\n{f(correct)}')


if __name__ == '__main__':
    unittest.main()