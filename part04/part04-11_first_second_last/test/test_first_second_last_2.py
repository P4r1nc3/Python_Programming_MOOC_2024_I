import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.first_second_last'

@points('4.first_second_last')
class ETjaVSanaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'en')

    def test_5_second_word_function_ok(self):
        for row in ["once upon a time there was a programmer", "happily ever after", "Lorem ipsum dolor sit amet consectetur adipiscing elit", "first second", "please write a program which keeps asking the user for words"]:
            with patch('builtins.input', side_effect=["2 2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.first_second_last import second_word
                
                try:
                    res = second_word(row)
                except:
                    self.assertTrue(False, f'Make sure, that function can be called as follows:\nsecond_word("{row}")') 
        
                output_all = get_stdout().replace(output_at_start, '', 1)

                expected = row.split(' ')[1]
                self.assertFalse(res == None, f'Calling second_word("{row}") should return\n{expected}\nnow it does not return anything. Make sure that you use return command in any cases in your function!')           
                self.assertEqual(res, expected, f'Calling second_word("{row}") should return\n{expected}\nnow it returns\n{res}')
                self.assertFalse(len(output_all)>0, f'Calling second_word("{row}") should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

    def test_6_last_word_exists(self):
        try:
            from src.first_second_last import last_word
        except:
            self.assertTrue(False, f'Your code should contain function named as last_word')
        try:
            from src.first_second_last import last_word
            last_word("once upon a time there was a programmer")
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows:\last_word("once upon a time there was a programmer")')

    def test_7_last_word_function_ok(self):
        for row in ["once upon a time there was a programmer", "happily ever after", "Lorem ipsum dolor sit amet consectetur adipiscing elit", "first second", "please write a program which keeps asking the user for words"]:
            with patch('builtins.input', side_effect=["2 2"] * 10):
                reload_module(self.module)
                output_at_start = get_stdout()
                from src.first_second_last import last_word
               
                try:
                     res = last_word(row)
                except:
                    self.assertTrue(False, f'Make sure, that function can be called as follows:\nlast_word("{row}")') 
                        
                output_all = get_stdout().replace(output_at_start, '', 1)

                odotettu = row.split(' ')[-1]
                self.assertFalse(res == None, f'Calling last_word("{row}") should return\n{odotettu}\nnow it does not return anything. Make sure that you use return command in any cases in your function!')           
                self.assertEqual(res, odotettu, f'Calling last_word("{row}") should return\n{odotettu}\nnow it returns\n{res}')
                self.assertFalse(len(output_all)>0, f'Calling last_word("{row}") should not print out anything, but it prints out\n{output_all}\nremove print commands inside function')

if __name__ == '__main__':
    unittest.main()