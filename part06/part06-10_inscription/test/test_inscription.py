import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.inscription'

def format(a):
    return "\n".join(a)

def get_content(file):
    with open(file) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

@points('6.inscription')
class InscriptionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["Arto", "omistettu.txt"]*10):
           cls.module = load_module(exercise, 'en')
    
    def test_inscription_works(self):
        for name, file in [
                ("Arto", "inscription.txt"),
                ("Lea", "inscr.txt"),
                ("John Doe", "book_cover_page.txt"),
                ("Sebastian", "arm.txt"),
                ("Jori", "foobar.txt"),
            ]:
            with patch('builtins.input', side_effect=[name, file, AssertionError("Your program has too many inputs")]):
                reload_module(self.module)
                output = get_stdout()
                
                try:
                    content = get_content(file)
                except:
                    mssage = """\nPlease note, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
                    self.assertTrue(False, f"With input values{name}\n{file}\nyour program should write the inscription into file {file}\n{mssage}")


                correct = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
                self.assertTrue(len(content) == 1, f"File {file} show have one row, now the content is:\n{format(content)}")
                self.assertTrue(content[0].strip() == correct, f"The content of the {file} should be \n{correct}\nbut it is \n{format(content)}")

if __name__ == '__main__':
    unittest.main()
