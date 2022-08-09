import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.star_studded'

@points('4.star_studded')
class StarStuddedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["x"]):
            cls.module = load_module(exercise, 'en')

    def test_inputs(self):
        values = "hei test longer abcde ellohello programminglanguage".split()
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = list("".join([x + "*" for x in test_case]))

                mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
                #\n{mssage}")   
                self.assertTrue(len(output)>0, f"Your program does not print out anything with the input {test_case}\n{mssage}")
                self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {test_case}")
                r = 1
                for l1,l2 in zip(output_list, cor):
                    self.assertEqual(l1.strip(), l2, 
                        f"On row {r} your program should print out\n{l2} \nbut now it prints out\n{11}\nwhen the input is {test_case}")
                    r += 1

if __name__ == '__main__':
    unittest.main()