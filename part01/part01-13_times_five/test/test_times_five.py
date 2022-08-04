import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.times_five'

@points('1.times_five')
class TimesFiveTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_times_three(self):
        with patch('builtins.input', return_value = '3'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Your program does not print anything' )
            self.assertTrue('15' in output, 'Output is incorrect with input 3, your program\'s output is\n' + output)
            expected = '3 times 5 is 15'
            assert_ignore_ws(self, output, expected,  'Your program\'s output is incorrect with input 3', 'en')

    def test_times_five(self):
        with patch('builtins.input', return_value = '5'):
            reload_module(self.module)
            output = get_stdout()
            expected = '5 times 5 is 25'
            assert_ignore_ws(self, output, expected,  'Your program\'s output is incorrect with input 5', 'en')

    def test_times_hundred(self):
        with patch('builtins.input', return_value = '100'):
            reload_module(self.module)
            output = get_stdout()
            expected = '100 times 5 is 500'
            assert_ignore_ws(self, output, expected,  'Your program\'s output is incorrect with input 100', 'en')

    def test_input_is_asked_only_once(self):
        with patch('builtins.input', return_value = '0') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Input should be asked exactly once.')

if __name__ == '__main__':
    unittest.main()
