import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.students_in_groups'

@points('1.students_in_groups')
class StudentsInGroupsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '1'):
            cls.module = load_module(exercise, 'en')

    def test_A_8_ja_4(self):
        with patch('builtins.input', side_effect = [ '8', '4', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'The program is expected to ask input two times.')
            expected = "Number of groups formed: 2"
            self.assertTrue(len(output)>0, "Your program does not print anything.")
            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 8 and 4 your program is expected to printout:\n{}\nyour program's output was:\n{}".format(expected, output))
            
    def test_B_11_ja_3(self):
        with patch('builtins.input', side_effect = [ '11', '3', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Number of groups formed: 4"
            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 11 and 3 your program is expected to printout:\n{}\nyour program's output was:\n{}".format(expected, output))

    def test_C_200_ja_99(self):
        with patch('builtins.input', side_effect = [ '200', '99', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Number of groups formed: 3"
            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 200 and 99 your program is expected to printout:\n{}\nyour program's output was:\n{}".format(expected, output))
            
    def test_D_53_ja_11(self):
        with patch('builtins.input', side_effect = [ '53', '11', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Number of groups formed: 5"
            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 53 and 11 your program is expected to printout:\n{}\nyour program's output was:\n{}".format(expected, output))
            
if __name__ == '__main__':
    unittest.main()
