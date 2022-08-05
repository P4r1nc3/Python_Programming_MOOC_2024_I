import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.story'

def p(a):
    return "\n".join(a)

testset = [
    ['hello', 'world', 'end'],
    'Once upon a time there was a girl'.split(' ') + ['end'],
    'It was a dark and stormy night'.split(' ') + ['end'],
    'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ') + ['end'],
    'The focus of the course is on programming and you will learn how to write programs and understand how they work For example the basics of algorithms control structures subprograms object-oriented programming are covered The grading is based on weekly exercises and an online exam'.split(' ') + ['end']
]

testset2 = [
    ['hello', 'world', 'world'],
    'Once upon a time there was a girl'.split(' ') + ['girl'],
    'It was a dark and stormy night'.split(' ') + ['night'],
    'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ') + ['aliqua'],
    'The focus of the course is on programming and you will learn how to write programs and understand how they work For example the basics of algorithms control structures subprograms object-oriented programming are covered The grading is based on weekly exercises and an online exam'.split(' ') + ['exam']
]

class StoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["end"] * 10):
           cls.module = load_module(exercise, 'en')

    @points('2.story-part1')
    def test_part1a(self):
        values = "hello hello end".split(" ")
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()  
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input\n{}".format(p(values)))

    @points('2.story-part1')
    def test_part1b(self):
       for *start, end  in testset:
        with patch('builtins.input', side_effect= start + [end, AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(start) + "\n" + end

            expected = ' '.join(start)
            self.assertTrue(len(output)>0, f"Your program did not print out anything with the input\n{inpt}" )
            self.assertEqual(expected.strip(), output.strip(), f"With the input\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

    @points('2.story-part2')
    def test_part2a(self):
        values = "hello hello".split(" ")
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()  
            except:
                self.assertTrue(False, "Make sure that execution of your program stops with the input\n{}".format(p(values)))

    @points('2.story-part2')
    def test_part2b(self):
       for *start, end in testset2:
        with patch('builtins.input', side_effect= start + [end, AssertionError("Input is asked too many times.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(start) + " " + end

            expected = ' '.join(start)
            self.assertEqual(expected.strip(), output.strip(), f"With the input\n{inpt}\nyour program should print out:\n{expected}\nyour program printed out:\n{output}" )

if __name__ == '__main__':
    unittest.main()