import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.emoticon'
@points('1.emoticon')
class EmoticonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_print_emoticon(self):
        reload_module(self.module)
        output = get_stdout()
        self.assertTrue(output.startswith(":"), "Make sure that you don't print out extra characters before the emoticon starts.")
        self.assertTrue(output.endswith(")"), "Make sure that you don't print out extra characters after the emoticon ends.")
        self.assertEqual(output, ":-)", "Emoticon is malformed.")

if __name__ == '__main__':
    unittest.main()
    