import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.print_a_single_line'

@points('1.print_a_single_line')
class PrintASingleLineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = "5 + 8 - 4 = 9"

        self.assertTrue(len(output) == 1, "Instead of one row, your program's output was in " + str(len(output)) + " rows.")
        self.assertEqual(output[0], correct, "Output is incorrect: it should be\n{}\nbut it is\n{}".format(correct, output[0]))            
   
if __name__ == '__main__':
    unittest.main()
