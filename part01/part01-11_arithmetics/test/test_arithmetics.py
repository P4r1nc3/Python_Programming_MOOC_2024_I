import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.arithmetics'

@points('1.arithmetics')
class ArithmeticsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = self.generate(27,15)

        self.assertTrue(len(output) == 4, "Instead of 4 rows, your program prints " + str(len(output)) + " rows.")
        for i in range(4):
            self.assertEqual(output[i].rstrip(), correct[i], "Output in row {} is incorrect: it should be\n{}\nbut it was\n{}".format((i + 1), correct[i], output[i]))
        
    def generate(self, x, y):
        s = [""] * 4
        s[0] = "{} + {} = {}".format(x, y, (x + y))
        s[1] = "{} - {} = {}".format(x, y, (x - y))
        s[2] = "{} * {} = {}".format(x, y, (x * y))
        s[3] = "{} / {} = {}".format(x, y, (x / y))
        return s
   

if __name__ == '__main__':
    unittest.main()
