import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.gift_tax_calculator'

@points('2.gift_tax_calculator')
class GiftTaxCalculatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'en')

    def test_values(self):
        values = ["11400 612", "42450 3445", "195000 21500", "567800 77270", "10100200 1689134"]
        for valuegroup in values:
            testvalue, correct = valuegroup.split(" ")
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(valuegroup.split(' ')[0]))

                self.assertTrue(len(output) == 1, "Instead of one row your program's output is in {} rows: {} when input is {}".format(len(output), output, testvalue))

                expected_output = "Amount of tax: " + str(float(correct)) + " euros"
                self.assertTrue(output[0].strip().find("Amount of tax: ")  > -1, "Output was\n{}\nExpected output is\n{}\when input is {}".
                    format(output[0], expected_output, testvalue))
                index = output[0].strip().find("Amount of tax: ")+len("Amount of tax: ")
                number = [x for x in output[0].strip()[index:].split(' ') if len(x)>0][0]
                self.assertTrue(number.find(correct) > -1, "Output\n{}\ndoes not contain correct result\n{}\nwhen input is {}".
                    format(output[0], expected_output, testvalue))

    def test_no_tax(self):
        values = [str(randint(0, 4999)) for i in range(5)]
        for testvalue in values:
            correct = "No tax"
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Your program does not print out anything with input {}".format(testvalue.split(' ')[0]))

                self.assertTrue(len(output) == 1, "Instead of one row your program's output is in {} rows: {} when input is {}".format(len(output), output, testvalue))
                self.assertTrue(output[0].lower().strip().find(correct.lower()) > -1, "Output\n{}\ndoes not contain correct result\n{}\nwhen input is {}".
                    format(output[0], correct, testvalue))
    
if __name__ == '__main__':
    unittest.main()
