import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.print_code'

@points('1.print_code')
class PrintCodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_output(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')
        correct = 'print("Hello there!")'

        self.assertFalse(len(output) == 0, "Your code does not print anything :(")
        self.assertEqual(len(split_output), 1, "Output contains extra lines.")
        self.assertTrue(output.count('print') == 1, f"Output is missing print command. Output was\n{output}\nExpected output is\n{correct}")
        self.assertTrue(output.count('"') == 2, f"Output does not contain quotation marks. Output was\n{output}\nExpected output is\n{correct}")
        self.assertEqual(output, correct, f"Output is incorrect. Output was\n{output}\nExpected output is\n{correct}")

if __name__ == '__main__':
    unittest.main()
