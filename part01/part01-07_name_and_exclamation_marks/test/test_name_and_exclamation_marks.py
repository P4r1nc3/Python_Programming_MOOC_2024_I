import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.name_and_exclamation_marks'

@points('1.name_and_exclamation_marks')
class NameAndExclamationMarksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_input_1(self):
        with patch('builtins.input', return_value = 'Paul'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Your code does not print anything!")
            assert_ignore_ws(self, output, '!Paul!Paul!', 'Your program does not work properply with input: Paul\n', 'en')

    def test_print_input_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            assert_ignore_ws(self,output, '!Ada!Ada!', 'Your program does not work properply with input: Ada\n', 'en')

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
