import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint
from inspect import getsource

exercise = 'src.countdown'

@points('2.countdown')
class CountdownTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_prints_right(self):
        reload_module(self.module)
        output = get_stdout()
        output_lines = output.split('\n')

        self.assertEqual(7, len(output_lines), "The number of rows printed out by the program is incorrect")

        self.assertEqual(output_lines[0], "Countdown!", "first row of print out is incorrect, your program's prints out\n"+ output)
        self.assertEqual(output_lines[1], "5", "second row of print out is incorrect\n"+ output)
        self.assertEqual(output_lines[2], "4", "third row of print out is incorrect\n"+ output)
        self.assertEqual(output_lines[3], "3", "fourth row of print out is incorrect\n"+ output)
        self.assertEqual(output_lines[4], "2", "fifth row of print out is incorrect\n"+ output)
        self.assertEqual(output_lines[5], "1", "sixth row of print out is incorrect\n"+ output)
        self.assertEqual(output_lines[6], "Now!", "seventh row of print out is incorrect\n"+ output)

    def test_prints_in_loop(self):
        source = getsource(self.module)
        p = 0
        for line in source.split("\n"):
            if line.strip().startswith("#"):
                continue
            if "print" in line:
                p += 1
        self.assertTrue(p<4, "There should be no more than three print commands in your code!. Now there are " + str(p) + " print commands.")

if __name__ == '__main__':
    unittest.main()
