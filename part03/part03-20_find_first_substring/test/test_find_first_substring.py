import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.find_first_substring'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(s : str, m: str) -> str:
    a = [s[i : i + 3] for i in range(0, len(s) - 2 ) if s[i] == m]
    if len(a) == 0:
        return ""
    return a[0]
   
@points('3.find_first_substring')
class FindFirstSubstringTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["incomprehensibilities","i"]):
            cls.module = load_module(exercise, 'en')
                

    def test_words_1(self):
        words = "incomprehensibilities,i abcccabd,a pineapple,p puppet,p simsalabim,s".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"The execution of your program fails with the input {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  + word)

                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{}\nwith the input ({})".
                    format(output_all, correct, testcase))

    def test_words_2(self):
        words = "swisswristwatch,s programminglanguage,g abcdefg,x nearanearanearerearanearlyeerieear,e islitthesheetthesheetislitandontheslittedsheetisit,i".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"The execution of your program fails with the input {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{}\ndoes not match with the correct print out \n{}\nwith the input ({})".
                    format(output_all, correct, testcase))

    def test_words_3(self):
        words = "python,o monkey,e".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"The execution of your program fails with the input {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                self.assertTrue(len(output_all)==0, f"Your program should not print out anything with the input {testcase}\nbut it printed out\n{output_all}")
  
if __name__ == '__main__':
    unittest.main()