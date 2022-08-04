import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.name_and_age'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.name_and_age')
class NameAndAgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_frances_fictitous(self):
        with patch('builtins.input', side_effect = [ 'Frances Fictitous', '1990', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Your program does not print anything' )
            e = 'Hi Frances Fictitous, you will be 31 years old at the end of the year 2021'
            assert_ignore_ws(self, output, e, "When input is Frances Fictitous 1990\n", 'en')

    def test_other_names_1(self):
        testset = [
            ['Paul Python', '2020', '1'],
        ]
        for name, born, age in testset:
            with patch('builtins.input', side_effect = [name, born]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hi {name}, you will be {age} years old at the end of the year 2021"
                assert_ignore_ws(self, output, e, f"When input is {name} {born}\n", 'en')

    def test_other_names_2(self):
        testset = [
            ['Angela Merkel', '1954', '67'],
        ]
        for name, born, age in testset:
            with patch('builtins.input', side_effect = [name, born]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hi {name}, you will be {age} years old at the end of the year 2021"
                assert_ignore_ws(self, output, e, f"When input is {name} {born}\n", 'en')

    def test_other_names_3(self):
        testset = [
            ['Wendy Rose', '2013', '8'],
        ]
        for name, born, age in testset:
            with patch('builtins.input', side_effect = [name, born]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hi {name}, you will be {age} years old at the end of the year 2021"
                assert_ignore_ws(self, output, e, f"When input is {name} {born}\n", 'en')

if __name__ == '__main__':
    unittest.main()
