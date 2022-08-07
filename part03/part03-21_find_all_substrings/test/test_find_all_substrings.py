import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.find_all_substrings'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(s : str, m: str) -> str:
    return "\n".join([s[i : i + 3] for i in range(0, len(s) - 2 ) if s[i] == m])
   

@points('3.find_all_substrings')
class FindAllSubstringsTest(unittest.TestCase):
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
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input " + word)  
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == cor_len, f"Instead of {cor_len} rows, your program prints out with the input ({testcase}) {len(output)} rows. The correct print out is\n{correct}")
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{output_all}\ndoes not match with the correct print out\n{correct}\nwith the input ({testcase})")

    def test_words_2(self):
        words = "swisswristwatch,s programminglanguage,g nearanearanearerearanearlyeerieear,e nearanearanearerearanearlyeerieear,a islitthesheetthesheetislitandontheslittedsheetisit,i".split(" ")
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
            
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == cor_len, f"Instead of {cor_len} rows, your program prints out with the input ({testcase}) {len(output)} rows. The correct print out is\n{correct}")
                self.assertTrue(outputs_equal(output_all, correct), "Your program's print out\n{output_all}\ndoes not match with the correct print out\n{correct}\nwith the input ({testcase})")
    
    def test_words_3(self):
        words = "python,o monkey,e abcdefg,x".split(" ")
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
            
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == 0, f"Your program should not print out anything with the input {testcase}\nbut it printed out\n{output_all}")

if __name__ == '__main__':
    unittest.main()