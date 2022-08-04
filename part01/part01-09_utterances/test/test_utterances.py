import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.utterances'

@points('1.utterances')
class UtterancesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        pieces = "simsala bimsala bim"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Your program printed " + str(len(output)) + " rows, instead of one row")
            self.assertTrue(output.count("-") == 2, f"Output should contain two hyphens (-), now output contains {output.count('-')} hyphens.")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Part " + piece + " was not included in output" +f" when input was {pieces}")
            self.assertTrue(output.strip().count(" ") == 0, "Output contains extra spaces.")
            vast = pieces.replace(" ", "-")+"!"
            self.assertTrue(output == vast, f"Output differs from the example.\nOutput was\n{output}\nExpected output was\n{vast}\nWhen input was\n{pieces}")

    def test_print_2(self):
        pieces = "hally tully yallah"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Your program printed " + str(len(output)) + " rows, instead of one row")
            self.assertTrue(output.count("-") == 2, "Output did not contain two hyphens (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Part " + piece + " was not included in output")
            self.assertTrue(output.strip().count(" ") == 0, "Output contains extra spaces.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Output differs from the example.")
    
    def test_print_3(self):
        pieces = "hocus pocus filiocus"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Your program printed " + str(len(output)) + " rows, instead of one row")
            self.assertTrue(output.count("-") == 2, "Output did not contain two hyphens (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Part " + piece + " was not included in output")
            self.assertTrue(output.strip().count(" ") == 0, "Output contains extra spaces.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Output differs from the example.")
    
if __name__ == '__main__':
    unittest.main()
