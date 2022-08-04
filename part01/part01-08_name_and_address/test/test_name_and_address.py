import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.name_and_address'

@points('1.name_and_address')
class NameAndAddressTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        test_input = "Peter,Python,1 Python Road,Pythoncity PY 37"
        test_output = "Peter Python,1 Python Road,Pythoncity PY 37".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            out = get_stdout()
            self.assertTrue(len(out)>0, "Your program did not print anything") 
            output = out.split("\n")
            self.assertTrue(len(output) == 3, "Your program printed " + str(len(output)) + " rows, instead of 3 rows")
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"First row of printout is incorrect.\nExpected\n{test_output[0]}\nRow was\n{output[0]}\nInput was\n{test_input}")
            for i in range(1,3):
                self.assertEqual(output[i], test_output[i], 'Row {} was incorrect with inputs {}'.format((i + 1), test_input))
    
    def test_print_2(self):
        test_input = "Alf,Newlyinvented,123 Invention Road,Newtown HR6 0WG"
        test_output = "Alf Newlyinvented,123 Invention Road,Newtown HR6 0WG".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Your program printed " + str(len(output)) + " rows, instead of 3 rows")
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"First row of printout is incorrect.\nExpected\n{test_output[0]}\nRow was\n{output[0]}\nInput was\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], 'Row {} was incorrect with inputs {}'.format((i + 1), test_input))
 
    def test_print_3(self):
        test_input = "Mary Poppins,Imaginaryperson,555 Mind Street apartment 234,Tampester CO5 6GF"
        test_output = "Mary Poppins Imaginaryperson,555 Mind Street apartment 234,Tampester CO5 6GF".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Your program printed " + str(len(output)) + " rows, instead of 3 rows")         
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"First row of printout is incorrect.\nExpected\n{test_output[0]}\nRow was\n{output[0]}\nInput was\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], 'Row {} was incorrect with inputs {}'.format((i + 1), test_input))

if __name__ == '__main__':
    unittest.main()
