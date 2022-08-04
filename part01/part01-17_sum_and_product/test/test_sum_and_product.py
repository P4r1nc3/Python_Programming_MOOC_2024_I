import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.sum_and_product'

@points('1.sum_and_product')
class SumAndProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_three_and_seven(self):
        with patch('builtins.input', side_effect = [ '3', '7', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.failIf(prompt.call_count < 2, 'The program is expected to ask input two times.')
            self.assertTrue(len(output)>0, 'Your program does not print anything.' )
            self.assertTrue('10' in output, 'The program does not print the sum of the numbers 3 and 7 correctly. Expected: 10'+ '\noutput was\n'+ str(output))
            self.assertTrue('21' in output, 'The program does not print the product of the numbers 3 and 7 correctly. Expected: 21'+ '\noutput was\n'+ str(output))
            expected = f"The sum of the numbers: 10"

            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 3 and 7 program's output is expected to contain row\n{}\nyour program's output was\n{}".format(expected, output))
            expected = f"The product of the numbers: 21"
            self.assertTrue(sanitize(expected) in sanitize(output), "With inputs 3 and 7 program's output is expected to contain row\n{}\nyour program's output was\n{}".format(expected, output))
            
    def test_additional_tests(self):
        testset = [
            ['0', '0'],
            ['0', '1'],
            ['13', '4'],
            ['7', '191'],
            ['716', '28213']
        ]
        for a, b in testset:
            with patch('builtins.input', side_effect = [ a, b, AssertionError("Input is asked too many times.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                sum =  int(a) + int(b)
                prod = int(a) * int(b)
                inputs = f"{a} ja {b}"
                self.assertTrue(str(sum) in output, 'With inputs {} the sum is incorrectly calculated. Expected: {}'.format(inputs, sum))
                self.assertTrue(str(prod) in output, 'With inputs {} the product is incorrectly calculated. Expected: {}'.format(inputs, prod))
                expected = f"The sum of the numbers: {sum}"
                self.assertTrue(sanitize(expected) in sanitize(output), "With inputs {} your program is expected to printout: {}".format(inputs, expected))
                expected = f"The product of the numbers: {prod}"
                self.assertTrue(sanitize(expected) in sanitize(output), "With inputs {} your program is expected to printout: {}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
