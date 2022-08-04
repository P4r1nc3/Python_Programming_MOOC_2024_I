import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.calculator'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output
#add, multiply,subtract(-)
@points('1.calculator')
class CalculatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_add1(self):
        with patch('builtins.input', side_effect = [ '1', '2', 'add', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '1 + 2 = 3'
            self.assertTrue(len(output)>0, "Your program does not print out anything with inputs 1, 2, add")
            self.assertTrue(expect in output, f"With inputs 1, 2, add your program should have printed out\n{expect}\nYour program printed out:\n{output}")

    def test_add2(self):
        with patch('builtins.input', side_effect = [ '75', '23', 'add', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Your program does not print out anything with inputs 75, 23, add")
            expect = '75 + 23 = 98'
            self.assertTrue(expect in output, f"With inputs 75, 23, add your program should have printed out\n{expect}\nYour program printed out:\n{output}")

    def test_subtract1(self):
        with patch('builtins.input', side_effect = [ '2', '1', 'subtract', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Your program does not print out anything with inputs 2, 1, subtract")
            expect = '2 - 1 = 1'
            self.assertTrue(expect in output, f"With inputs 2, 1, subtract your program should have printed out\n{expect}\nYour program printed out:\n{output}")

    def test_subtract2(self):
        with patch('builtins.input', side_effect = [ '13', '34', 'subtract', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '13 - 34 = -21'
            self.assertTrue(expect in output, f"With inputs 13, 34, subtract your program should have printed out\n{expect}\nYour program printed out:\n{output}")

    def test_multiply1(self):
        with patch('builtins.input', side_effect = [ '2', '3', 'multiply', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '2 * 3 = 6'
            self.assertTrue(len(output)>0, "Your program does not print out anything with inputs 2, 3, multiply")
            self.assertTrue(expect in output, f"With inputs 2, 3, multiply your program should have printed out\n{expect}\nYour program printed out:\n{output}")
   
    def test_multiply2(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'multiply', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '27 * -3 = -81'
            self.assertTrue(expect in output, f"With inputs 27, -3, multiply your program should have printed out\n{expect}\nYour program printed out:\n{output}")

    def test_xcrap(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'quotient', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) == 0, f"With inputs 27, -3, quotient your program should not print out anything\nYour program printed out:\n{output}")

if __name__ == '__main__':
    unittest.main()
