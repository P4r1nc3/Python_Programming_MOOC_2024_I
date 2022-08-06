import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.underlining'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def f(d):
    return ' '.join(d) + " (empty)"

@points('3.underlining')
class UnderliningTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["no", '']):
            cls.module = load_module(exercise, 'en')

    def test_1_execution_ends_with_empty_string(self):
        words = "python attempt".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, "Make sure that the execution of the program stops with the input {}".format(f(words)))

    def test_2_two_words(self):
        words = "python attempt".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Input is asked too many times.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"With the input {f(words)}, instead of {len(words)*2} rows, your program's output is in {len(output)} rows:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Print out in row {i+1} is incorrect, it should be\n{e}\nrow is\n{line}\noutput is:\n{output_all}")

    def test_3_many_words(self):
        words = "test hiya simsalabim zorro woo-hoo!".split(" ")
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Input is asked too many times.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"With the input {f(words)}, instead of {len(words)*2} rows, your program's output is in {len(output)} rows:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Print out in row {i+1} is incorrect, it should be\n{e}\nrow is\n{line}\noutput is:\n{output_all}")

    def test_4_many_sentences(self):
        words = ["Hello everybody", "Ello hello everybody!", "This is a longer test sencence", "How will this go? - we will see it soon...", "One more test: test!!"]
    
        with patch('builtins.input', side_effect = words+ ['', AssertionError("Input is asked too many times.")]):
            reload_module(self.module)
            output_all = get_stdout()
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
    
            self.assertEqual(len(words)*2, len(output), f"With the input {f(words)}, instead of {len(words)*2} rows, your program's output is in {len(output)} rows:\n{output_all}")
            for i in range(len(output)):
                line = output[i]
                if i%2==1:
                    e = '-'*len(words[i//2])
                    self.assertEqual(line, e, f"Print out in row {i+1} is incorrect, it should be\n{e}\nrow is\n{line}\noutput is:\n{output_all}")


if __name__ == '__main__':
    unittest.main()
