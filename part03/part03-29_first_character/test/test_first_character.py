import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source

exercise = 'src.first_character'

@points('3.first_character')
class FirstCharacterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_function_exists(self):
        with patch('builtins.input', side_effect=["2"] * 10):
            try:
                self.module.first_character("testing")
            except:
                self.assertTrue(False, f'Your code should contain function named as first_character, which can be called as follows:\nfirst_character("testing")')

    def test_correct_characters(self):
        for word in ["python", 'javascript', 'xyz', 'coder', 'vacation', 'night', 'programming', 'apple']:
          with patch('builtins.input', side_effect=["2"] * 10):   
            reload_module(self.module)
            output_at_start = get_stdout()
            self.module.first_character(word)
            output = get_stdout().replace(output_at_start, '', 1).replace('\n', '')
            self.assertTrue(len(output)>0, f'Calling function first_character("{word}") does not print out anything')
            self.assertEqual(1, len(output), f'Function call first_character("{word}") should print out only one character, now it printed out {len(output)} characters, print out was\n{output}')
            self.assertEqual(word[0], output, f'Function call first_character("{word}") should print out only one character, {word[0]}, now it printed out\n{output}')

if __name__ == '__main__':
    unittest.main()
