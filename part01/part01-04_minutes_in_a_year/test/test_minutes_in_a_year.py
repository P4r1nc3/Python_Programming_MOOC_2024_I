import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.minutes_in_a_year'

@points('1.minutes_in_a_year')
class MinutesInAYearTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'en')

    def test_output(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')

        # self.assertEqual(len(split_output), 1, "Output contains extra lines.")
        self.assertTrue(output.find("525600") > -1, "Output does not contain correct amount of minutes.")

if __name__ == '__main__':
    unittest.main()
