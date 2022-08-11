import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.spellchecker'

def f(d):
    return '\n'.join(d)

import os
from shutil import copyfile

testdata = ["wordlist.txt"]

@points('6.spellchecker')
class SpellcheckerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['This is me']):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_1_stops(self):
        inpt = "This is me"
        with patch('builtins.input', side_effect = [inpt, AssertionError("Too many inputs.")]):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, f"Ensure that program stops with input\n{inpt}")     

    def test_2_toimii(self):
        for inpt, good in [
                ("This is me", "This is me"),
                ("We use ptython to make a spell checker", "We use *ptython* to make a spell checker"),
                ("this is acually a good and usefull program","this is *acually* a good and *usefull* program"),
                ("Questions we additions is extremely incommode","Questions we additions is extremely incommode"),
                ("As in merry at forth least ye stood","As in merry at forth least ye stood"),
                ("And cold sonss yet with","And cold *sonss* yet with"),
                ("Delivered middletony therefore me at","Delivered *middletony* therefore me at"),
                ("Attachment companions mann way excellence how her pianoforte","Attachment companions *mann* way excellence how her pianoforte"),
                ("Frankness applaued by supported ye household","Frankness *applaued* by supported ye household"),
                ("Collected favourite nowe for for and rapturous replsive consulted","Collected *favourite* *nowe* for for and rapturous *replsive* consulted"),
                ("An seems green bee wrote again","An seems green bee wrote again"),
                ("She add what ownn onli like","She add what *ownn* *onli* like"),
                ("Tolerably we as extremity exquiste do commanded","Tolerably we as extremity *exquiste* do commanded"),
                ("Doubtful offended do entrance of landloord moreover is mistress in","Doubtful offended do entrance of *landloord* moreover is mistress in"),
                ("Nay was appear entire ladyes","Nay was appear entire *ladyes*"),
                ("Sportsman do allowance is setember shameless am sincrity oh recommend","Sportsman do allowance is *setember* shameless am *sincrity* oh recommend"),
                ("Gate tell man dayz that who","Gate tell man *dayz* that who"),
                ("Not far stufff she think the jokes","Not far *stufff* she think the jokes"),
                ("Going as by do knwn noise he wrote round leave","Going as by do *knwn* noise he wrote round leave"),
                ("Warmly putt branch peope narrow see","Warmly putt branch *peope* narrow see"),
                ("Winding its waiting yett parlors marryed own feeling","Winding its waiting *yett* parlors *marryed* own feeling"),
                ("Marry fruit do spite zokes an times","Marry fruit do spite *zokes* an times"),
                ("Whether at it anknown varrant herself winding if","Whether at it *anknown* *varrant* herself winding if"),
                ("Him same nne name sake had post love","Him same *nne* name sake had post love"),
                ("An busy feel form hant am up help","An busy feel form *hant* am up help"),
                ("Parties it brother amonzst an fortune of","Parties it brother *amonzst* an fortune of"),
                ("Twenty pehind wicket why age now itself ten","Twenty *pehind* wicket why age now itself ten"),
            ]:
            with patch('builtins.input', side_effect = [inpt, AssertionError("Too many inputs.")]):
                try:
                    reload_module(self.module)
                    output = get_stdout().strip()
                except:
                    self.assertTrue(False, f"Ensure that program stops with input\n{inpt}")
            
                mssage = """\nNotice, that in this program NO CODE should be included inside
if __name__ == "__main__":
block
"""
            #\n{mssage}") 
                self.assertTrue(len(output)>0, f"Your program does not output anything with input\n{inpt}\n{mssage}") 
                self.assertEqual(good, output, f"The output of your program:\n{output}\nis wrong, expected:\n{good}\ninput was:\n{inpt}")

if __name__ == '__main__':
    unittest.main()
