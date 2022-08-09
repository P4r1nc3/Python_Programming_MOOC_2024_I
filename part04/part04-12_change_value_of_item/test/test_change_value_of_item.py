import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.change_value_of_item'

def f(d):
    return '\n'.join(d)

def getcor(l):
    ls = list(range(1, 6))
    i = 0
    s = []
    while l[i] != -1:
        ls[l[i]] = l[i+1]
        i += 2
        s.append(str(ls))
    return s


@points('4.change_value_of_item')
class ChangeValueOfItemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["-1"]):
            cls.module = load_module(exercise, 'en')

    def test_inputs_1(self):
        values = (0,100,-1)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)

            mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
            #\n{mssage}") 

            self.assertTrue(len(output)>0, f"Your program does not print out anything when the input is {values}\n{mssage}") 
            self.assertEqual(len(output_list), len(cor), f"Your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows, when the input is: {values}")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1.strip(), l2.strip(), 
                    f"The print out in row {r}: is incorrect, program should print out\n{l1}\nbut it prints out\n{l2}\nwhen the input is {values}")
                r += 1

    def test_inputs_2(self):
        values = (1,25,3,333,2,-543,-1)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"Your program should print out {len(cor)} rows, now it prints out {len(output_list)} rows, when the input is: {values}")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1.strip(), l2.strip(), 
                    f"The print out in row {r}: is incorrect, program should print out\n{l1}\nbut it prints out\n{l2}\nwhen the input is {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()
