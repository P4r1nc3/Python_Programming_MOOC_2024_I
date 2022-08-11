import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.city_bikes'

def f(d):
    return '\n'.join(d)

function1 = "get_station_data"
function2 = "distance"

import os
from shutil import copyfile

testdata = [f"stations{i}.csv" for i in range(1,10)]

def close(a, b):
   return abs(a-b)<0.001

@points('6.city_bikes_part_1')
class CityBikesPart1Test(unittest.TestCase):
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

    def test_0_main_ok(self):
        ok, line = check_source(self.module)
        message = """Code testing the functions must be included inside
if __name__ == "__main__":
block. The following code needs to be relocated::
"""
        self.assertTrue(ok, message+line)

    def test_1_get_station_data_exists(self):
            try:
                from src.city_bikes import get_station_data
            except:
                self.fail('Your code should contain function get_station_data(filename: str)')

            try:   
                get_station_data("stations1.csv")
            except Exception as e:
                self.assertTrue(False, 'Function call get_station_data("stations1.csv") throws an error ' + e)

    def test_2_get_station_data_return_type(self):
        get_station_data = load(exercise, function1, 'en')
        val = get_station_data("stations1.csv")
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Function {function1} should return a dictionary, now it returns a value {val} which is of type {taip}.")

    def test_3_get_station_data_works(self):
        exp = {'Kaivopuisto': (24.950292890004903, 60.15544479374228), 'Laivasillankatu': (24.956347471358754, 60.16095909388713), 'Kapteeninpuistikko': (24.944927399779715, 60.15818919997167), 'Viiskulma': (24.941775800312996, 60.16098589997938), 'Sepankatu': (24.93628529982675, 60.157948300373846), 'Hietalahdentori': (24.92970990039163, 60.162225100108344), 'Designmuseo': (24.94595999955436, 60.163103199952786), 'Vanha kirkkopuisto': (24.939149900447603, 60.165288299815245), 'Erottajan aukio': (24.944134928883898, 60.16691166693994)}
        get_station_data = load(exercise, function1, 'en')
        val = get_station_data("stations1.csv")
        code = 'get_station_data("stations1.csv")'

        for a, k in exp.items():
            self.assertTrue(a in val, f'Dictionary returned by {code} should contain key {a}. Now function returns\n{val}')
            taip = str(type(val[a])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a]), tuple, f'Key {a} returned by {code} should be a tuple\nnow it is {val[a]}\nand the type is {taip}')
            taip = str(type(val[a][0])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a][0]), float, f'The key {a} returned by {code} should contain coordinates of type float.\nNow the value is {val[a][0]} and the type is {taip}')
            taip = str(type(val[a][1])).replace("<class '", '').replace("'>","")
            self.assertEqual(type(val[a][1]), float, f'The key {a} returned by {code} should contain coordinates of type float.\nNow the value is {val[a][1]} and the type is {taip}')
            self.assertEqual(k, val[a], f'The value of the key {a} returned by {code} should be\n{k}\nnow it was\n{val[a]}')
            self.assertEqual(sorted(list(val.keys())), sorted(list(exp.keys())), f'The dictionary returned by {code} should contain the following keys:\n{sorted(list(exp.keys()))}\nnow the returned keys are:\n{sorted(list(val.keys()))}')

    def test_4_distance_exists(self):
        try:
            from src.city_bikes import distance
        except:
            self.assertTrue(False, 'Code should contain function distance(stations: dict, station1: str, station2: str)')
       
        try:
            load_station_data = load(exercise, function1, 'en')
            stations = load_station_data("stations1.csv")
            val = distance(stations, "Kaivopuisto", "Laivasillankatu")
            code = """stations = get_station_data("stations1.csv")
distance(stations, "Kaivopuisto", "Laivasillankatu")"""
        except Exception as ioe:
            self.assertTrue(False, 'Function call {koodi} threw an error\n'+ ioe)

    def test_5_distance_return_type(self):
        load_station_data = load(exercise, function1, 'en')
        distance = load(exercise, function2, 'en')
        stations = load_station_data("stations1.csv")
        val = distance(stations, "Kaivopuisto", "Laivasillankatu")
        code = """stations = get_station_data("stations1.csv")
distance(stations, "Kaivopuisto", "Laivasillankatu")"""

        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == float, f"Function {function2} should return a float type value, now it returns  {val} which is of type {taip}.")

    def test_6_distance_works(self):
        for start, end, dist in [
            ("Kaivopuisto","Laivasillankatu",0.6985294572684413),
            ("Kaivopuisto","Kapteeninpuistikko",0.42549272615780437),
            ("Kaivopuisto","Viiskulma",0.7753594392019532),
            ("Kaivopuisto","Sepankatu",0.8225989080090765),
            ("Kaivopuisto","Hietalahdentori",1.3646193733314156),
            ("Kaivopuisto","Designmuseo",0.884633872724747),
            ("Kaivopuisto","Vanha kirkkopuisto",1.2559087786511032),
            ("Kaivopuisto","Erottajan aukio",1.3197416922973566),
            ("Laivasillankatu","Kaivopuisto",0.6985294572684413),
            ("Laivasillankatu","Kapteeninpuistikko",0.7022284848835603),
            ("Laivasillankatu","Viiskulma",0.805236059266575),
            ("Laivasillankatu","Sepankatu",1.158086391801006),
            ("Laivasillankatu","Hietalahdentori",1.478708873076181),
            ("Laivasillankatu","Designmuseo",0.6215590959138332),
            ("Laivasillankatu","Vanha kirkkopuisto",1.06531462356818),
            ("Laivasillankatu","Erottajan aukio",0.9452984144177514),
            ("Kapteeninpuistikko","Kaivopuisto",0.42549272615780437),
            ("Kapteeninpuistikko","Laivasillankatu",0.7022284848835603),
            ("Kapteeninpuistikko","Viiskulma",0.3564371848513532),
            ("Kapteeninpuistikko","Sepankatu",0.47831316747614694),
            ("Kapteeninpuistikko","Hietalahdentori",0.9531836845512406),
            ("Kapteeninpuistikko","Designmuseo",0.5494080311763683),
            ("Kapteeninpuistikko","Vanha kirkkopuisto",0.851536068409486),
            ("Kapteeninpuistikko","Erottajan aukio",0.970926409204973),
            ("Viiskulma","Kaivopuisto",0.7753594392019532),
            ("Viiskulma","Laivasillankatu",0.805236059266575),
            ("Viiskulma","Kapteeninpuistikko",0.3564371848513532),
            ("Viiskulma","Sepankatu",0.454038196553383),
            ("Viiskulma","Hietalahdentori",0.6808521499981444),
            ("Viiskulma","Designmuseo",0.3299938171568305),
            ("Viiskulma","Vanha kirkkopuisto",0.49994836657660163),
            ("Viiskulma","Erottajan aukio",0.6717172315531527),
            ("Sepankatu","Kaivopuisto",0.8225989080090765),
            ("Sepankatu","Laivasillankatu",1.158086391801006),
            ("Sepankatu","Kapteeninpuistikko",0.47831316747614694),
            ("Sepankatu","Viiskulma",0.454038196553383),
            ("Sepankatu","Hietalahdentori",0.5985018458531813),
            ("Sepankatu","Designmuseo",0.7838427337497422),
            ("Sepankatu","Vanha kirkkopuisto",0.8314166229661707),
            ("Sepankatu","Erottajan aukio",1.0870235918079745),
            ("Hietalahdentori","Kaivopuisto",1.3646193733314156),
            ("Hietalahdentori","Laivasillankatu",1.478708873076181),
            ("Hietalahdentori","Kapteeninpuistikko",0.9531836845512406),
            ("Hietalahdentori","Viiskulma",0.6808521499981444),
            ("Hietalahdentori","Sepankatu",0.5985018458531813),
            ("Hietalahdentori","Designmuseo",0.9032737292463177),
            ("Hietalahdentori","Vanha kirkkopuisto",0.6230173508383396),
            ("Hietalahdentori","Erottajan aukio",0.9523680841254529),
            ("Designmuseo","Kaivopuisto",0.884633872724747),
            ("Designmuseo","Laivasillankatu",0.6215590959138332),
            ("Designmuseo","Kapteeninpuistikko",0.5494080311763683),
            ("Designmuseo","Viiskulma",0.3299938171568305),
            ("Designmuseo","Sepankatu",0.7838427337497422),
            ("Designmuseo","Hietalahdentori",0.9032737292463177),
            ("Designmuseo","Vanha kirkkopuisto",0.4479532398935395),
            ("Designmuseo","Erottajan aukio",0.43534463863879497),
            ("Vanha kirkkopuisto","Kaivopuisto",1.2559087786511032),
            ("Vanha kirkkopuisto","Laivasillankatu",1.06531462356818),
            ("Vanha kirkkopuisto","Kapteeninpuistikko",0.851536068409486),
            ("Vanha kirkkopuisto","Viiskulma",0.49994836657660163),
            ("Vanha kirkkopuisto","Sepankatu",0.8314166229661707),
            ("Vanha kirkkopuisto","Hietalahdentori",0.6230173508383396),
            ("Vanha kirkkopuisto","Designmuseo",0.4479532398935395),
            ("Vanha kirkkopuisto","Erottajan aukio",0.32935101970694375),
            ("Erottajan aukio","Kaivopuisto",1.3197416922973566),
            ("Erottajan aukio","Laivasillankatu",0.9452984144177514),
            ("Erottajan aukio","Kapteeninpuistikko",0.970926409204973),
            ("Erottajan aukio","Viiskulma",0.6717172315531527),
            ("Erottajan aukio","Sepankatu",1.0870235918079745),
            ("Erottajan aukio","Hietalahdentori",0.9523680841254529),
            ("Erottajan aukio","Designmuseo",0.43534463863879497),
            ("Erottajan aukio","Vanha kirkkopuisto",0.32935101970694375),    
            ]:
            get_station_data = load(exercise, function1, 'en')
            distance = load(exercise, function2, 'en')
            stations = get_station_data("stations1.csv")
            val = distance(stations, start, end)
            code = 'stations = get_station_data("stations1.csv")\n'+f'distance(stations, "{start}", "{end}")'

            self.assertTrue(close(val, dist), f"The answer {val} returned by function is wrong, it should be {dist} when called with\n{code}")

if __name__ == '__main__':
    unittest.main()
