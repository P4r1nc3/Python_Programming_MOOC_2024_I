import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.list_twice'

def getcor(values: tuple):
    s = []
    l = []
    for v in values[:-1]:
        l.append(int(v))
        s.append(f"The list now: {l}")
        s.append(f"The list in order: {sorted(l)}")
    return s + ["Bye!"]

@points('4.list_twice')
class ListTwiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["0"]):
            cls.module = load_module(exercise, 'en')

    def test_inputs_1(self):
        values = tuple("1 2 3 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)

            mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
            #\n{mssage}")   
            self.assertTrue(len(output.strip())>0, f"Your program does not print out anything with the input {values}\n{mssage}")
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r} your program should print out\n{l2} \nbut now it prints out\n{l1}\nwhen the input is {values}")
                r += 1

    def test_inputs_2(self):
        values = tuple("9 8 7 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertTrue(len(output.strip())>0, f"Your program does not print out anything with the input {values}")
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r} your program should print out\n{l2} \nbut now it prints out\n{l1}\nwhen the input is {values}")
                r += 1

    def test_inputs_3(self):
        values = tuple("9 1 8 2 7 3 11 12 22 21 0".split())
        with patch('builtins.input', side_effect = list(values)):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertTrue(len(output.strip())>0, f"Your program does not print out anything with the input {values}")
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r} your program should print out\n{l2} \nbut now it prints out\n{12}\nwhen the input is {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()