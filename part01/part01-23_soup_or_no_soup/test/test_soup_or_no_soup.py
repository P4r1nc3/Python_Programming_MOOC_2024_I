import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.soup_or_no_soup'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

def correct_order(output):
    parts = output.split("\n")
    cost = False
    for part in parts:
        if 'The total cost is' in part:
            cost = True
        if "Next please!" == part and not cost:
            return False

    return True  

@points('1.soup_or_no_soup')
class SoupOrNoSoupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_1_kramer_1(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '1', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Next please!"
            self.assertTrue(len(output)>0, f"Your program does print anything.")
            self.assertTrue(expected in output, f"With input Kramer, 1 your program should print out\n{expected}\nyour program printed out\n"+ output)
            expected = 'The total cost is 5.9'
            self.assertTrue(expected in output, f"With input Kramer, 1 your program should print out\n{expected}\nyour program printed out\n"+ output)
            self.assertTrue(correct_order(output), f"With input Kramer, 1 your program should print out\n'Next please!' following the print out of the cost\nyour program printed out\n"+ output)

    def test_2_kramer_4(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '4', AssertionError("Input is asked too many times.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Next please!"
            self.assertTrue(expected in output, f"With input Kramer, 4 your program should print out\n{expected}\nyour program printed out\n"+ output)
            expected = 'The total cost is 23.6'
            self.assertTrue(expected in output, f"With input Kramer, 4 your program should print out\n{expected}\nyour program printed out\n"+ output)
            self.assertTrue(correct_order(output), f"with input Kramer, 4 your program should print out\n'Next please!' following the print out of the cost\nyour program printed out\n"+ output)

    def test_3_jerry(self):
        with patch('builtins.input', side_effect = [ 'Jerry', AssertionError("Input was asked too many times when first input was Jerry.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Next please!"
            self.assertTrue(expected in output, f"With input Jerry your program should print out\n{expected}\nyour program printed out\n"+ output)

    def test_4_jane_doe(self):
        with patch('builtins.input', side_effect = [ 'Jane Doe', '2', AssertionError("Input is asked too many times when name is Jane Doe.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Next please!"
            self.assertTrue(expected in output, f"with input Jane Doe, 2 your program should print out\n{expected}\nyour program printed out\n"+ output)
            expected = 'The total cost is 11.8'
            self.assertTrue(expected in output, f"with input Jane Doe, 2 your program should print out\n{expected}\nyour program printed out\n"+ output)

if __name__ == '__main__':
    unittest.main()
