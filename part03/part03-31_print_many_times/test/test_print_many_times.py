import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.print_many_times'

@points('3.print_many_times')
class PrintManyTimesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["exam","2"]):
           cls.module = load_module(exercise, 'en')
           
    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_function_exists(self):
        with patch('builtins.input', side_effect=[AssertionError("Asking for input from the user is not expected in this exercise")]):
            try:
                clear_stdout()
                self.module.print_many_times("test",2)
            except:
                self.assertTrue(False, f'Your code should contain function named as print_many_times, which can be called as follows:\nprint_many_times("test", 2)')

    def test_print_out_correct(self):
        test_data = [
            ("test", 2), ("python", 7), ("All Pythons, except one, grow up", 5), ("introduction to programming", 4),  ("advanced course in programming", 12),
            ("And in one day, all the pythonians, learned how to use function to print out cool things countless times", 10), ("final test", 20)
        ]

        for mj, lkm in test_data:
          with patch('builtins.input', side_effect=[AssertionError("Asking for input from the user is not expected in this exercise")]):
            reload_module(self.module)
            output_at_start = get_stdout()
            clear_stdout()
            self.module.print_many_times( mj, lkm)
            output_all = get_stdout().replace(output_at_start, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            self.assertTrue(len(output_all)>0, f'Function call print_many_times("{mj}", {lkm}) does not print out anything')
            acual = '\n'.join(output)
            self.assertEqual(lkm, len(output), f'Function call print_many_times("{mj}", {lkm}) should print out {lkm} rows, now it printed out {len(output)} rows, print out was\n{acual}')
            for i in range(lkm):
                self.assertEqual(mj, output[i].strip(), f'Each row which function call print_many_times("{mj}", {lkm}) prints out, should be {mj}, following row is incorrect:\n{output[i]}\nwhole print out of the function was:\n{acual}')

if __name__ == '__main__':
    unittest.main()