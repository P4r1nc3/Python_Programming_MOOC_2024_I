import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.seconds_in_a_day'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.seconds_in_a_day')
class SecondsInADayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1_seconds_in_one_day(self):
        with patch('builtins.input', return_value = '1'):
            reload_module(self.module)
            result = get_stdout()
            self.assertTrue(len(result)>0, 'Your program does not print anything' )
            self.assertTrue('86400' in result.split(), '1 day is 86400 seconds. Your program\'s output was: ' + parse_result(result))

    def test_2_seconds_in_seven_days(self):
        with patch('builtins.input', return_value = '7'):
            reload_module(self.module)
            result = get_stdout()
            self.assertTrue('604800' in result.split(), '7 days is 604800 seconds. Your program\'s output was: ' + parse_result(result))


    def test_3_additional_tests(self):
        testset = [
            ['0', '0'],
            ['13', '1123200'],
            ['51', '4406400'],
            ['110', '9504000'],
            ['2020', '174528000']
        ]
        for days, seconds in testset:
            with patch('builtins.input', return_value = days):
                reload_module(self.module)
                self.assertTrue(seconds in get_stdout().split(), 'Output is incorrect with input ' + days + '. ' + days + ' days is ' + seconds + ' seconds.')

if __name__ == '__main__':
    unittest.main()
