import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.city_bikes'

def f(d):
    return '\n'.join(d)

function1 = "get_station_data"
function2 = "greatest_distance"

import os
from shutil import copyfile

testdata = [f"stations{i}.csv" for i in range(1,10)]

def close(a, b):
   return abs(a-b)<0.001

@points('6.city_bikes_part_2')
class CityBikesPart2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Input was not expected")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'en')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_1_greatest_distance_exicsts(self):
        try:
            from src.city_bikes import greatest_distance
        except:
            self.fail('Your code should contain function greatest_distance(stations: dict)')
       
        try:
            code = """stations = get_station_data("stations1.csv")
greatest_distance(stations)"""
            get_station_data = load(exercise, function1, 'en')
            stations = get_station_data("stations1.csv")
            val = greatest_distance(stations)

        except Exception as ioe:
            self.assertTrue(False, f'Function {code} threw an error\n{ioe}')

    def test_2_greatest_distance_return_type(self):
        code = """stations = get_station_data("stations1.csv")
greatest_distance(stations)"""
        get_station_data = load(exercise, function1, 'en')
        greatest_distance = load(exercise, function2, 'en')
        stations = get_station_data("stations1.csv")
        val = greatest_distance(stations)

        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == tuple, f"Function {function2} should return a tuple, now it returns {val} which is of type {taip}.")
        taip = str(type(val[0])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[0]) == str, f"The first item in a tuple returned by {function2} should be a string, now the type is {taip}\nReturn value was {val}")
        taip = str(type(val[1])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[1]) == str, f"The second item in a tuple returned by {function2} should be a string, now the type is {taip}\nReturn value was {val}")       
        taip = str(type(val[2])).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val[2]) == float or type(val[2]) == int , f"The third item in a tuple returned by {function2} should be a float, now the type is {taip}\nReturn value was {val}")

    def test_3_greatest_distance_works(self):
        for filename, answer in [
            ("stations1.csv", ("Laivasillankatu", "Hietalahdentori", 1.478708873076181)),
            ("stations2.csv", ("Puistokaari", "Karhulantie", 14.817410024304905)),
            ("stations3.csv", ("Puotinkylan kartano", "Friisilanaukio", 21.971314423058754)),
            ("stations4.csv", ("Kaivopuisto", "Linnuntie", 11.569340603194116)),
            ("stations5.csv", ("Puotinkylan kartano", "Etuniementie", 21.8490934564622)),
            ("stations6.csv", ("Karhulantie", "Haukilahdenranta", 19.566890288851994)),
            ("stations7.csv", ("Karhulantie", "Tiistinkallio", 21.848686409979116)),
            ("stations8.csv", ("Puotinkylan kartano", "Etuniementie", 21.8490934564622)),
            ("stations9.csv", ("Voikukantie", "Friisilanaukio", 20.834906297083204)),
        ]:
            code = f'stations = get_station_data("{filename}")\ngreatest_distance(stations)'
            get_station_data = load(exercise, function1, 'en')
            greatest_distance = load(exercise, function2, 'en')
            stations = get_station_data(filename)
            a1, a2, et = greatest_distance(stations)
            pal = (a1, a2, et)
            ma1, ma2, met = answer

            self.assertTrue((a1 == ma1 and a2 == ma2) or (a2 == ma1 and a1 == ma2), f'Answer is wrong when executed code is \n{code}\nLongest distance is between stations {ma1} and {ma2}\nYour function returns {pal}')
            self.assertTrue(close(et, met), f'Answer is wrong when executed code is\n{code}\nLongest distance is {met}\nYour function returns {pal}')

if __name__ == '__main__':
    unittest.main()
