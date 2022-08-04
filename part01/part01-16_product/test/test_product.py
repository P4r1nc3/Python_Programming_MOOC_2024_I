import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce

exercise = 'src.product'

@points('1.product')
class ProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = "0,0,0".split(",")):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        inputs = "1,2,3"
        with patch('builtins.input', side_effect = inputs.split(",")):
            reload_module(self.module)
            output = get_stdout().strip()
            ilist = [int(x) for x in inputs.split(",")]
            correct = "The product is " + str(reduce(lambda x,y: x * y, ilist))
            self.assertTrue(len(output.split("\n")) == 1, "Instead of one row, your program's output is now in " + str(len(output.split("\n"))) + " rows.")
            self.assertEqual(sanitize(output), sanitize(correct), "Program's output was\n{}\nwhen it was expected to be\n{}\nwith inputs {}".format(output, correct, inputs))
            
    def test_print_2(self):
        inputs = "7,2,14"
        with patch('builtins.input', side_effect = inputs.split(",")):
            reload_module(self.module)
            output = get_stdout().strip()
            ilist = [int(x) for x in inputs.split(",")]
            correct = "The product is " + str(reduce(lambda x,y: x * y, ilist))
            self.assertTrue(len(output.split("\n")) == 1, "Instead of one row, your program's output is now in " + str(len(output.split("\n"))) + " rows.")
            self.assertEqual(sanitize(output), sanitize(correct), "Program's output was\n{}\nwhen it was expected to be\n{}\nwith inputs {}".format(output, correct, inputs))
            
if __name__ == '__main__':
    unittest.main()
