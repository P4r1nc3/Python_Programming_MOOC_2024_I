import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.second_occurrence'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace("  ", " ") == str2.lower().replace("  ", " ")

def get_correct(s : str, s2: str) -> str:
    if s.find(s2) > -1:
        return s.find(s2, s.find(s2) + len(s2))
    else:
        return -1

def f(m):
    return "\n".join(m.split(","))

@points('3.second_occurrence')
class SecondOccurrenceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["abcdabcdabcd","abc"]):
           cls.module = load_module(exercise, 'en')

    def test_2_or_more_is_found(self):
        words = "abcdabcdabcd,abc simsalabim,im ac/dc,c ToBeOrNotToBe,Be nearanearanearerearanearlyeerieear,near shesellsseashells,ells abababa,aba".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Make sure that your program works with the input " + word)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                
                correct = get_correct(word, char)
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  +  f(testcase))
                self.assertTrue(len(output) == 1, "Instead of {} rows, your program prints out {} rows with the input {}\n{}".
                    format(1, len(output), testcase, output_all))
                
                self.assertTrue(str(correct) in output_all, "Correct answer {} is not found from the print out when the input is\n{}\nThe program printed out:\n{}". 
                    format(correct, f(testcase), output_all))

                correct_str = "The second occurrence of the substring is at index " + str(correct) + "."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Your program's print out\n{}\ndoes not match with the correct print out\n{} \nwhen the input is ({})".
                    format(output_all, correct_str, testcase))

    def test_only_1_is_found(self):
        words = "london,lon abcdabcd,bcda abracadabra,cad dumdumdadadada,dumda".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Make sure that your program works with the input " +  f(testcase))
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input "  +  f(testcase))
                self.assertTrue(len(output) == 1, "Instead of {} rows, your program prints out {} rows with the input {}\n{}".
                    format(1, len(output), testcase, output_all))
                
                correct_str = "The substring does not occur twice in the string."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Your program's print out\n{}\ndoes not match with the correct print out\n{} \nwhen the input is ({})".
                    format(output_all, correct_str, testcase))

    def test_nothing_is_found(self):
        words = "simsalabim,harrypotter abcdabcd,abcde totallyempty,void 123454321,3212".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Make sure that your program works with the input " +  f(testcase))
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
            
                self.assertFalse(len(output_all)==0, "Your program does not print out anything with the input\n"+f(testcase))
                self.assertTrue(len(output) == 1, "Instead of {} rows, your program prints out {} rows with the input {}\n{}".
                    format(1, len(output), testcase, output_all))
                
                correct_str = "The substring does not occur twice in the string."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Your program's print out\n{}\ndoes not match with the correct print out\n{} \nwhen the input is ({})".
                    format(output_all, correct_str, testcase))

if __name__ == '__main__':
    unittest.main()