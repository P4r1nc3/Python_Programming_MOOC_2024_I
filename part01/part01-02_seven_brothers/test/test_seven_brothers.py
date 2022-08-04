import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.seven_brothers'
@points('1.seven_brothers')
class SevenBrothersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_content(self):
        reload_module(self.module)
        split_output = get_stdout().split('\n')
        self.assertEqual(len(split_output), 7, 'Output was expected to have {0} lines, your program\'s output is now in {1} lines.'.format(7, len(split_output)))
        correct = "Aapo Eero Juhani Lauri Simeoni Timo Tuomas".split()
        for i in range(7):
            self.assertEqual(split_output[i], correct[i], "Line {0} in output is incorrect.".format(i + 1))

if __name__ == '__main__':
    unittest.main()
    