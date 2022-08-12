import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.spellchecker_2'

def f(d):
    return '\n'.join(d)

import os
from shutil import copyfile

testdata = ["wordlist.txt"]

def line_starting(wrong, lines):
    for line in lines:
        if line.strip().startswith(wrong):
            return line

    return None

@points('7.spellchecker_version2')
class SpellcheckerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['This iss me']):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test1_stops(self):
        inpt = "This iss me"
        with patch('builtins.input', side_effect = [inpt, AssertionError("Input is asked too many times.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Make sure, that the execution of the program stops with the input\n{inpt}")     

    def test2_works(self):
        for inpt, good, corrections in [
                ("This iis good", "This *iis* good", ["iis: iris, ibis, is"]),
                ("We use ptython to make a spell checker", "We use *ptython* to make a spell checker", ["ptython: python, pythons, typhon"]),
                ("this is acually a good and usefull program","this is *acually* a good and *usefull* program", ["acually: actually, tactually, factually", "usefull: usefully, useful, museful"]),
                ("And cold sonss yet with","And cold *sonss* yet with", ["sonss: sons, sonless, songs", ]),
                ("Delivered middletony therefore me at","Delivered *middletony* therefore me at", ["middletony: milton, middle, midden", ]),
                ("Attachment companions mann way excellence how her pianoforte","Attachment companions *mann* way excellence how her pianoforte", ["mann: manna, man, ann", ]),
                ("Frankness applaued by supported ye household","Frankness *applaued* by supported ye household", ["applaued: applauded, applaud, applause"]),
                ("She add what ownn onli like","She add what *ownn* *onli* like", ["ownn: own, owning, town", "onli: yoni, soli, only", ]),            
                ("Gate tell man dayz that who","Gate tell man *dayz* that who", ["dayz: day, dray, daze", ]),
                ("Winding its waiting yett parlors marryed own feeling", "Winding its waiting *yett* parlors *marryed* own feeling", ["yett: yet, yeti, layette", "marryed: marred, married, arrayed" ])
            ]:
            with patch('builtins.input', side_effect = [inpt, AssertionError("Input is asked too many times.")]):
                try:
                    reload_module(self.module)
                    output = get_stdout().strip()
                except:
                    self.assertTrue(False, f"Make sure, that execution of the program ends with the following input\n{inpt}")
            
                
                msg = 'Note, that in this program no code must not be placed inside the if __name__ == "main" -block.'

                self.assertTrue(len(output)>0, f"Your program does not print out anything with the input\n{inpt}\n{msg} ")
                outLines = output.split('\n')
                self.assertEqual(good.strip(), outLines[0].strip(), f"First row of the print out of your program:\n{outLines[0]}\nis incorrect, expected:\n{good}\ninput was:\n{inpt}")
                for c in corrections:
                    wrong = c.split(':')[0]
                    line = line_starting(wrong, outLines)
                    self.assertFalse(line == None, f"Your program is expected to suggest corrections for the word {wrong} when the input is:\n{inpt}")
    
                    try:
                        line.split(':')[1]
                    except:
                          self.assertFalse(True, f"Your program is expected to suggest corrections for the word {wrong} when the input is:\n{inpt}, only following row was found\n{line}\nwhich however is not in accordance with the assignment")

                    suggestions = [ x.strip() for x in line.split(':')[1].split(',')]
                    betterments = [ x.strip() for x in c.split(':')[1].split(',')]
                    distinct = set(suggestions).isdisjoint(set(betterments))
                    self.assertFalse(distinct, f"Your program should provide reasonable suggestions for correction og the word {wrong}. Suggestions were {suggestions}\nexpected {betterments}")

if __name__ == '__main__':
    unittest.main()