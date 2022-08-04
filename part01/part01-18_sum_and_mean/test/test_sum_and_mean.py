import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.sum_and_mean'

@points('1.sum_and_mean')
class SumAndMeanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1234(self):
        with patch('builtins.input', side_effect = [ '1', '2', '3', '4', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 4, 'The program is expected to ask input four times.')
            self.assertTrue(len(output)>0, 'Your program does not print anything.')
            self.assertTrue('10' in output, 'The program does not print the sum of the numbers 1, 2, 3 and 4 correctly. Expected: 10'+ '\noutput was\n'+ str(output))
            self.assertTrue('2.5' in output, 'The program does not print the mean of the numbers 1, 2, 3 and 4 correctly. Expected: 2.5'+ '\noutput was\n'+ str(output))
            expected = "The sum of the numbers is 10 and the mean is 2.5"
            self.assertTrue(sanitize(expected) in sanitize(output), "with inputs 1, 2, 3 and 4 program is expected to print\n{}\nyour program's output was\n{}".format(expected, output))
            

    def test_additional_tests(self):
        testset = [
            [ '3', '7', '2', '8' ],
            [ '8', '-22', '75', '5' ],
            [ '0', '0', '0', '0' ],
        ]
        for a, b, c, d in testset:
            with patch('builtins.input', side_effect = [ a, b, c, d, AssertionError("Input is asked too many times.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                sum =  int(a) + int(b) + int(c) + int(d)
                avg = sum / 4
                inputs = f"{a}, {b}, {c} and {d}"
                self.assertTrue(str(sum) in output, 'With inputs {} the sum is incorrectly calculated. Expected: {}'.format(inputs, sum))
                self.assertTrue(str(avg) in output, 'With inputs {} the mean is incorrectly calculated. Expected: {}'.format(inputs, avg))
                expected = f"The sum of the numbers is {sum} and the mean is {avg}"
                self.assertTrue(sanitize(expected) in sanitize(output), "With inputs {} your program is expected to printout: \n{}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
