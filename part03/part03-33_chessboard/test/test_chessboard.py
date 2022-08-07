import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.chessboard'

@points('3.chessboard')
class ChessboardTest(unittest.TestCase):
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
        
    def test_funktio_olemassa(self):
        try:
            clear_stdout()
            self.module.chessboard(2)
        except:
            self.assertTrue(False, f"Your code should contain function named as chessboard, which can be called as follows: chessboard(2)")
    
    def test_board(self):
        with patch('builtins.input', side_effect=["2"] * 100):
            for size in range(3, 60):
                reload_module(self.module)
                output_at_start = get_stdout()
                clear_stdout()
                self.module.chessboard(size)
                output_all = get_stdout().replace(output_at_start, '', 1)
                
                output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

                self.assertTrue(len(output_all)>0, f"Function call chessboard({size}) does not print out anything")
                acual = '\n'.join(output)
                self.assertEqual(size, len(output), f"Function call chessboard({size}) should print out {size} rows, now it printed out {len(output)} rows, print out was\n{acual}")
                for i in range(size):
                    row = "10"*size if i%2==0 else "01"*size
                    row = row[0:size]
                    self.assertEqual(row, output[i].strip(), f"Row {i}, which function call chessboard({size}) prints out, should be {row}, now it is\n{output[i]}\nwhole print out of the function was\n{acual}")

if __name__ == '__main__':
    unittest.main()