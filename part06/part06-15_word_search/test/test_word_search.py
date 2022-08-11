import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.word_search'
function = "find_words"

import os
from shutil import copyfile

def format(f):
    return "\n".join(f)

filename = "words.txt"

@points('6.word_search')
class WordSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not required")]):
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        os.remove(filename)

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions should be included in the 
if __name__ == "__main__":
block. The following code should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.word_search import find_words
        except:
            self.assertTrue(False, "Your program should contain a function word_search(search_term: str)")
        
        try:
            val = find_words("cat")
        except:        
            self.assertTrue(False, 'Plese ensure that the following function call works: word_search("cat")')         
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == list, f'Function word_search("cat") should return a list, now it returns {val} which is of type {taip}.')

    def test_2_search_no_special_chars(self):
        test_case = ("cat")
        correct = ["cat"]
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except OSError as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")
       
        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")

    def test_3_search_dots_1(self):
        test_case = ("ca.")
        correct = ['cab', 'cad', 'cal', 'cam', 'can', 'cap', 'car', 'cat', 'caw', 'cay']
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except Exception as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")

    def test_4_search_dots_2(self):
        test_case = ("c.d.")
        correct = ['cads', 'cede', 'cmdg', 'coda', 'code', 'cods', 'cuds']
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except Exception as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")
    
    def test_5_search_dots_3(self):
        test_case = ("a...e")
        correct = ['abase', 'abate', 'abide', 'abode', 'above', 'abuse', 'acute', 'adage', 'addle', 'adobe', 'adore', 'adoze', 'aerie', 'afire', 
        'afore', 'agape', 'agate', 'agave', 'agaze', 'aggie', 'agile', 'aglee', 'agone', 'agree', 'aisle', 'alate', 'algae', 'alice', 'alike', 
        'aline', 'alive', 'alone', 'amaze', 'amble', 'amice', 'amide', 'amire', 'amole', 'amove', 'ample', 'amuse', 'andre', 'anele', 'angle', 
        'anile', 'anise', 'ankle', 'annie', 'anode', 'anole', 'antre', 'apace', 'apple', 'aquae', 'arete', 'argle', 
        'argue', 'arise', 'arose', 'aside', 'atone', 'aurae', 'autre', 'awake', 'aware', 'awoke', 'axone', 'azide', 'azine', 'azole', 'azote', 'azure']
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except Exception as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")
    
    def test_6_search_asterisk_1(self):
        test_case = ("reson*")
        correct = ['resonance', 'resonances', 'resonant', 'resonantly', 'resonants', 'resonate', 'resonated', 
            'resonates', 'resonating', 'resonation', 'resonations', 'resonator', 'resonators']
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except Exception as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")
    
    def test_7_search_asterisk_2(self):
        test_case = ("*okes")
        correct = ['artichokes', 'backstrokes', 'blokes', 'breaststrokes', 'chokes', 'cokes', 'convokes', 
        'cowpokes', 'downstrokes', 'equivokes', 'evokes', 'heatstrokes', 'instrokes', 'invokes', 'jokes', 
        'keystrokes', 'pokes', 'provokes', 'reinvokes', 'revokes', 'sidestrokes', 'slowpokes', 
        'smokes', 'spokes', 'stokes', 'strokes', 'sunstrokes', 'tokes', 'unyokes', 'upstrokes', 'yokes']
        find_words = load(exercise, function, 'en')
        try:
            data = find_words(test_case)
        except Exception as ioe:
            self.assertTrue(False, f"There was an error with search term {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Search term {test_case} should return {len(correct)} lines, now the search returns {len(data)} lines: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Search term {test_case} should return lines \n{format(correct)} \nbut the function returned lines \n{format(data)}")
    
if __name__ == '__main__':
    unittest.main()
