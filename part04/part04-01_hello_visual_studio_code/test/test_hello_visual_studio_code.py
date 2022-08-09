import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import choice

exercise = 'src.hello_visual_studio_code'

def f(d):
    return '\n'.join(d)

@points('4.hello_visualstudio_code')
class VsCodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["emacs", "visual studio code"]):
            cls.module = load_module(exercise, 'en')

    def test_1_program_stops(self):
        words = "emacs;visual studio code".split(";")
    
        with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure that the execution of the program ends with the input\n{f(words)}")

    def test_2_functionality(self):
        for string in [
                "emacs;visual studio code", "word;emacs;notepad;visual studio code"
            ]:
            words = string.split(";")
        
            with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Make sure that the execution of the program ends with the input\n{f(words)}")

                mssage = """\nNote, that any code SHOULD NOT be placed inside if __name__ == "__main__": block
                """
                #\n{mssage}") 

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}\n{mssage}")

                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(words), len(output), f"Instead of {len(words)} rows, your programs print out is in {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}")
                for i in range(len(words)-2):
                    e = "not good" if not words[i] in ["word", "notepad"] else "awful"
                    line = output[i]
                    self.assertEqual(line, e, f"Row {i+1} in your programs print out is incorrect, it should be\n{e}\nrow is\n{line}\nwith the input:\n{f(words)}\nthe print out is:\n{output_all}")
                
                e = "an excellent choice!"
                line = output[-1]
                self.assertEqual(line, e, f"Last row of print out of your program is incorrect, it should be\n{e}\nrow is\n{line}\nwith the input:\n{f(words)}\the print out is:\n{output_all}")
                
    def test_3_case_insensitive(self):
        for i in range(20):
            vsdc = ""
            for l in "visual studio code":
                vsdc += choice([l, l.upper()])
            words = ["emacs", vsdc]
    
            with patch('builtins.input', side_effect = words + [ AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output_all = get_stdout()
                except:
                    self.assertTrue(False, f"Make sure that the execution of the program ends with the input\n{f(words)}")

                mssage = """\nNote, that any code SHOULD NOT be placed inside if __name__ == "__main__": block
                """
                #\n{mssage}") 

                self.assertTrue(len(output_all)>0, f"Your program does not print out anything with the input\n{f(words)}\n{mssage}")

                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                self.assertEqual(len(words), len(output), f"Instead of {len(words)} rows, your programs print out is in {len(output)} rows:\n{output_all}\nwith the input:\n{f(words)}")
                for i in range(len(words)-2):
                    e = "not good" if not words[i] in ["word", "notepad"] else "awful"
                    line = output[i]
                    self.assertEqual(line, e, f"Row {i+1} in your programs print out is incorrect, it should be\n{e}\nrow is\n{line}\nwith the input:\n{f(words)}\nthe print out is:\n{output_all}")
                
                e = "an excellent choice!"
                line = output[-1]
                self.assertEqual(line, e, f"Last row of print out of your program is incorrect, it should be\n{e}\nrow is\n{line}\nwith the input:\n{f(words)}\the print out is:\n{output_all}")
               

if __name__ == '__main__':
    unittest.main()
