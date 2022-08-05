import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.nephews'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.nephews')
class NephewsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_mickey(self):
        values = "Morty Ferdie".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Remove headers
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("one of Mickey Mouse's nephews") > -1, "From output {} mention 'one of Mickey Mouse's nephews' is not found when input is {}".
                    format(output[0], value))
                self.assertFalse(output[0].find("one of Donald Duck's nephews") > -1, "From output {} mention 'one of Donald Duck's nephews' is found when input is {}".
                    format(output[0], value))

    def test_donald(self):
        values = "Huey Dewey Louie".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Remove headers
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))


                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("one of Donald Duck's nephews") > -1, "From output {} mention 'one of Donald Duck's nephews' is not found when input is {}".
                    format(output[0], value))
                self.assertFalse(output[0].find("one of Mickey Mouse's nephews") > -1, "From output {} mention 'one of Mickey Mouse's nephews' is found when input is {}".
                    format(output[0], value))

    def test_other(self):
        values = "Ada Linus Steve".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Remove headers
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(value))

                self.assertTrue(len(output) == 1, "Instead of one row, your program's output is in {} rows: {} when input is {}".format(len(output), output, value))
                self.assertTrue(output[0].find("not a nephew of any character I know of") > -1, "From output {} mention 'not a nephew of any character I know of' is not found when input is {}".
                    format(output[0], value))
                
   
if __name__ == '__main__':
    unittest.main()
