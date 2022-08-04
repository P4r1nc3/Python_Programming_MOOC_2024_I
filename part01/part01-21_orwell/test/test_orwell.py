import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.orwell'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.orwell')
class OrwellTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1984(self):
        with patch('builtins.input', return_value = '1984'):
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(len(output)==0, "With input 1984 your program should print out Orwell\nYour program did not print anything")
            self.assertTrue('Orwell' in output, "With input 1984 your program should print out Orwell\nYour program printed out\n" + output )

    def test_additional_tests(self):
        testset = ['2020', '1983', '1985']
        for vuosi in testset:
            with patch('builtins.input', return_value = vuosi):
                reload_module(self.module)
                output = get_stdout()
                self.assertFalse(len(output)>0, f"With input {vuosi} program should not print out anything, your program printed out:\n"+ output)

if __name__ == '__main__':
    unittest.main()
