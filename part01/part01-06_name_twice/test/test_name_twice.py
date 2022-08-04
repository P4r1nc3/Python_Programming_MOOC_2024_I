import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.name_twice'

@points('1.name_twice')
class NameTwiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_input_1(self):
        with patch('builtins.input', return_value = 'Paul'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Your program does not print anything!")
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Paul' and splitted[1].rstrip() == 'Paul', f'Your program did not work properply with input: Paul. Output was\n{output}\nExpected output is\nPekka\nPekka')

    def test_print_input_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Ada' and splitted[1].rstrip() == 'Ada', f'Your program did not work properply with input: Ada. Output was\n{output}\nExpected output is\nAda\nAda')


    def test_input_is_asked_only_once(self):
        with patch('builtins.input', return_value = '') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Input should be asked exactly once.')

if __name__ == '__main__':
    unittest.main()
