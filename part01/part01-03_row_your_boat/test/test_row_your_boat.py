import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tmc import points

from tmc.utils import get_stdout, load_module, reload_module, assert_ignore_ws, sanitize

exercise = 'src.row_your_boat'
@points('1.row_your_boat')
class RowYourBoatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')
        
    def test_content(self):
        reload_module(self.module)
        out = get_stdout()
        self.assertTrue(len(out)>0, 'Your code does not print anything')
        split_output = sanitize(out).split('\n')

        self.assertFalse(len(split_output) != 4, 'Output was expected to have {0} lines, your program\'s output is now in {1} lines.'.format(4, len(split_output)))
        assert_ignore_ws(self, split_output[0], 'Row, row, row your boat,', 'The print out on the first line is incorrect.', 'en')
        assert_ignore_ws(self, split_output[1], 'Gently down the stream.', 'The print out on the second line is incorrect.', 'en')
        assert_ignore_ws(self, split_output[2], 'Merrily, merrily, merrily, merrily,', 'The print out on the third line is incorrect.', 'en')
        assert_ignore_ws(self, split_output[3], 'Life is but a dream.', 'The print out on the fourth line is incorrect.', 'en')

if __name__ == '__main__':
    unittest.main()