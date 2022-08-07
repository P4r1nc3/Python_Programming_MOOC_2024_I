import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source, clear_stdout

exercise = 'src.mean'

@points('3.mean')
class MeanTest(unittest.TestCase):
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
        with patch('builtins.input', side_effect=["2"] * 10):
            try:
                clear_stdout()
                self.module.mean(1, 2, 3)
            except:
                self.assertTrue(False, f'Your code should contain function named as mean, which can be called as follows:\nmean(1,2,3)')

    def test_calculation_is_correct(self):
        for l1, l2, l3 in [(5, 3, 1), (10, 1, 1), (1,1,2), (-3, 7, 21), (5, 44, 21), (0, 0, 0), (-9, 22, 1021)]:
          with patch('builtins.input', side_effect=["2"] * 10):
            reload_module(self.module)
            output_at_start = get_stdout()
            clear_stdout()
            self.module.mean(l1, l2, l3)
            output_all = get_stdout().replace(output_at_start, '', 1)
            
            output = [l for l in output_all.split("\n") if len(l.strip())>0 ]

            inpt = ', '.join(str(i) for i in [l1, l2, l3])

            self.assertTrue(len(output_all)>0, f"Calling function mean{inpt} does not print out anything")
            acual = '\n'.join(output)
            self.assertEqual(1, len(output), f"Function call mean({inpt}) should print out only 1 row, now it printed out {len(output)} rows, print out was\n{acual}")
            expctd = (l1+l2+l3) / 3
            try:
                was = float(acual.strip())
            except:
                self.assertFalse(True, f"Function call mean({inpt}) should print out {expctd}, print out of the function was\n{acual}\nis not convertible to a floating point number!")
           
            self.assertAlmostEqual(expctd, was, 2, f"Function call mean({inpt}) should print out {expctd}, now it printed out\n{was}")

if __name__ == '__main__':
    unittest.main()