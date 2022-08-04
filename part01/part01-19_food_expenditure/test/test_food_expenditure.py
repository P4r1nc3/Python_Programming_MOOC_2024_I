import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.food_expenditure'

@points('1.food_expenditure')
class FoodExpenditureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_0(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
             
            self.assertTrue(len(output)>0, 'Your program does print anything.' )
            self.assertFalse(prompt.call_count < 2, 'The program is expected to ask input three times.')
            expected = "Daily: 4.5 euros"
            self.assertTrue(sanitize(expected) in sanitize(output), f"With inputs 4, 2.5 and 21.5 output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")
            expected = "Weekly: 31.5 euros"
            self.assertTrue(sanitize(expected) in sanitize(output), f"With inputs 4, 2.5 and 21.5 output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")
            
    def test_1(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            
            self.assertFalse(prompt.call_count < 2, 'The program is expected to ask input three times.')
            expected = "Daily: 4.5 euros"
            self.assertTrue(sanitize(expected) in sanitize(output), f"With inputs 4, 2.5 and 21.5 output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")
            expected = "Weekly: 31.5 euros"
            self.assertTrue(sanitize(expected) in sanitize(output), f"With inputs 4, 2.5 and 21.5 output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")
                        
    def test_2_additional_tests(self):
        testset = [
            [ '5', '3.5', '43.75', '8.75', '61.25'], 
            [ '1', '2.25', '15.25', '2.5', '17.5' ],
            [ '0', '0', '0', '0.0', '0.0' ],
        ]
        for a, b, c, d, w in testset:
            with patch('builtins.input', side_effect = [ a, b, c, AssertionError("Input is asked too many times.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                inputs = f"{a}, {b}, and {c}"
                self.assertFalse(prompt.call_count < 3, 'The program should ask for input three times.')
                expected = f"Daily: {d} euros"
                self.assertTrue(sanitize(expected) in sanitize(output), f"with inputs {inputs} output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")
                expected = f"Weekly: {w} euros"
                self.assertTrue(sanitize(expected) in sanitize(output), f"With {inputs} output is expected to contain row:\n{expected}\nyour program's output was:\n{output}")

if __name__ == '__main__':
    unittest.main()
