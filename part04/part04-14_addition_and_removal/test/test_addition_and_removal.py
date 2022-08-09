import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.addition_and_removal'

def getcor(values: tuple):
    s = []
    l = []
    for v in values:
        s.append(f"The list is now {l}")
        if v == "d":
            l.append(len(l) + 1)
        elif v == "r":
            l.pop(len(l) - 1)
        else:
            s.append("Bye!")
    return s

@points('4.addition_and_removal')
class AdditionAndRemovalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["x"]):
            cls.module = load_module(exercise, 'en')

    def test_inputs_1(self):
        values = tuple("d d d x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure, that your program works when the input is {values}")                
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)

            mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
            #\n{mssage}")
            self.assertTrue(len(output.strip())>0, f"Your program does not print out anything when the input is {values}\n{mssage}")   
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r}, your program should print out\n{l2}\nbut now it prints out\n{l1}\nwhen the input is {values}")
                r += 1

    def test_syotteet2(self):
        values = tuple("d r d d d r r x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure that your program works when the input is {values}")      
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r}, your program should print out\n{l2}\nbut now it prints out\n{l1}\nwhen the input is {values}")
                r += 1

    def test_syotteet3(self):
        values = tuple("d d d d d r d r d x".split())
        with patch('builtins.input', side_effect = list(values)):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, f"Make sure that your program works when the input is {values}")      
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"In addition to asking for the inputs from the user, your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows when the input is {values}")
            r = 1
            for l1,l2 in zip(output_list, cor):
                self.assertEqual(l1.strip(), l2, 
                    f"On row {r}, your program should print out\n{l2}\nbut now it prints out\n{l1}\nwhen the input is {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()