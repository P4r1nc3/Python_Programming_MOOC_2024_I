import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source

exercise = 'src.square_of_hashes'

@points('3.square_of_hashes')
class SquareOfHashesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
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
            self.module.hash_square(1)
        except:
            self.assertTrue(False, f'Function hash_square is not found from your code or execution of the function is in infinite loop:\nTry: hash_square(1)')

    def test_square_ok(self):
        for size in [2, 3, 5, 7, 10, 13, 25, 80]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_at_start = get_stdout()
            self.module.hash_square(size)
            output_all = get_stdout().replace(output_at_start, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            self.assertTrue(len(output_all)>0, f"Function call hash_square({size}) does not print out anything")
            acual = '\n'.join(output)
            self.assertEqual(size, len(output), f"Function call hash_square({size}) should print out {size} rows, now it printed out {len(output)} rows, print out was\n{acual}")
            for i in range(size):
                self.assertEqual("#"*size, output[i].strip(), f"Each row which function call hash_square({size}) prints out, should be {'#'*size}, following row is incorrect\n{output[i]}\nwhole print out of the function was\n{acual}")

if __name__ == '__main__':
    unittest.main()