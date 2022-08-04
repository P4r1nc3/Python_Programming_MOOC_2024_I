import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.story'

@points('1.story')
class StoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'en')

    def test_print_1(self):
        pieces = "Jeremy,1340"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                
            self.assertTrue(len(output)>0, "Your program does not print anything with input\nJeremy\n1340")
                    
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Input " + piece + " was not included in output, when input was\nJeremy\n1340")
            
            story = plist[0] + " is valiant knight, born in the year " + plist[1] + "." 
            story += " One morning " + plist[0] + " woke up to an awful racket: a dragon was approaching the village. "
            story += "Only " + plist[0] + " could save the village's residents."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Output differs from the example with input\nJeremy\n1340\nOutput was:\n{}\nExpected output was:\n{}".format(output, story))

    def test_print_2(self):
        pieces = "Charles Dreadful,1119"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Input " + piece + " was not included in output, when input was\nCharles Dreadful\n1119")
            
            story = plist[0] + " is valiant knight, born in the year " + plist[1] + "." 
            story += " One morning " + plist[0] + " woke up to an awful racket: a dragon was approaching the village. "
            story += "Only " + plist[0] + " could save the village's residents."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Output differs from the example with input\nCharles Dreadful\n1119\nOutput was:\n{}\nExpected output was:\n{}".format(output, story))
            
    def test_print_3(self):
        pieces = "Arthur,1290"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Input " + piece + " was not included in output")
            
            story = plist[0] + " is valiant knight, born in the year " + plist[1] + "." 
            story += " One morning " + plist[0] + " woke up to an awful racket: a dragon was approaching the village. "
            story += "Only " + plist[0] + " could save the village's residents."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Output differs from the example with input\nArthur\n1290\nOutput was:\n{}\nExpected output was:\n{}".format(output, story))

if __name__ == '__main__':
    unittest.main()
