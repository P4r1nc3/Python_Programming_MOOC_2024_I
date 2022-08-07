import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, get_stdout, check_source, clear_stdout

exercise = 'src.seven_brothers'

@points('3.seven_brothers')
class SevenBrothersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_function_exists(self):
        try:
            clear_stdout()
            self.module.seven_brothers()
        except:
            self.assertTrue(False, f"Your code should contain function named as seven_brothers, which can be called as follows:\nseven brothers()")

    def test_seven(self):
        brothers = [
            "Aapo",
            "Eero",
            "Juhani",
            "Lauri",
            "Simeoni",
            "Timo",
            "Tuomas"
        ]
        clear_stdout()
        self.module.seven_brothers()
        output_all = get_stdout()
        output = output_all.split('\n')
        self.assertTrue(len(output_all)>0, f"Calling function seven_brothers does not print out anything")
        self.assertEqual(7, len(output), f"Function seven brothers should print out 7 rows when called, now it printed out {len(output)} rows, print out was\n{output_all}")
        for i in range(7):
             self.assertEqual(brothers[i], output[i].strip(), f"After calling function seven brothers, row {i+1} in the print out is expected to be\n{brothers[i]}\nbut it was\n{output[i]}")

if __name__ == '__main__':
    unittest.main()