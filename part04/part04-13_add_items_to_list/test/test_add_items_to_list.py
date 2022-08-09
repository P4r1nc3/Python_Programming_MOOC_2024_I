import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.add_items_to_list'

@points('4.add_items_to_list')
class AddItemsToListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["1","1"]):
            cls.module = load_module(exercise, 'en')
   
    def test_inputs_1(self):
        values = (2,100,200)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"In addition to asking for the inputs from the user, your program should print out one row, now it prints out {len(output_list)} rows, when the input is: {values}")
            mssage = """\nNote, that, in this exercise, any code SHALL NOT BE PLACED inside
if __name__ == "__main__":
block
            """
            #\n{mssage}")             
            
            self.assertTrue(len(output.strip())>0, f"Your program does not print out anything when the input is {values}\n{mssage}")
            self.assertEqual(output.strip(), cor, f"Your program should print out\n{cor} \nbut now it prints out\n{output}\nwhen the input is {values}")

    def test_inputs_2(self):
        values = (5,55,33,44,22,66)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"In addition to asking for the inputs from the user, your program should print out one row, now it prints out {len(output_list)} rows, when the input is: {values}")
            self.assertEqual(output.strip(), cor, f"Your program should print out\n{cor} \nbut now it prints out\n{output}\nwhen the input is {values}")

    def test_inputs_3(self):
        values = (7,-9,-6,-11,-24,45,23,0)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = str(list(values[1:]))
            self.assertEqual(len(output_list), 1, f"In addition to asking for the inputs from the user, your program should print out one row, now it prints out {len(output_list)} rows, when the input is: {values}")
            self.assertEqual(output.strip(), cor, f"Your program should print out\n{cor} \nbut now it prints out\n{output}\nwhen the input is {values}")
    
if __name__ == '__main__':
    unittest.main()
