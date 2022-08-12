import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.dice_roller'

@points('7.dice_roller')
class DiceRollerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0a_main_program_ok(self):
        ok, line = check_source(self.module)
        message = """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)
    
    def test1_function_roll_exists_and_return_value_is_correct(self):
        try:
             from src.dice_roller import roll
        except:
            self.assertTrue(False, f'Your code should contain function named as roll(die: str)')
        
        try:
            result = roll("A")
        except:
            self.assertTrue(False, f'Make sure, that following function call works roll("A")')

        try:
            result = roll("B")
        except:
            self.assertTrue(False, f'Make sure, that following function call works roll("B")')

        try:
            result = roll("C")
        except:
            self.assertTrue(False, f'Make sure, that following function call works roll("C")')        

        self.assertTrue(type(result) == int, f'Function roll does not return a integer, when executing the following code roll("A")')

    def test_2_correct_results_with_throws_die_A(self):
        from src.dice_roller import roll

        expected = [3, 6]
        count = {3:0, 6:0}
        times = 60000
        for i in range(times):
            result = roll("A")
            self.assertTrue(result in expected, f'When calling roll("A") result must be 3 or 6, now result was {result}')
            count[result] += 1

        n = 3
        m = 5
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("A") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

        n = 6
        m = 1
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("A") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

    def test_2_correct_results_with_throws_die_B(self):
        from src.dice_roller import roll

        expected = [2, 5]
        count = {2:0, 5:0}
        times = 60000
        for i in range(times):
            result = roll("B")
            self.assertTrue(result in expected, f'When calling roll("B") result must be 2 or 5, now result was {result}')
            count[result] += 1

        n = 2
        m = 3
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("B") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

        n = 5
        m = 3
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("B") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

    def test_2_correct_results_with_throws_die_C(self):
        from src.dice_roller import roll

        expected = [1, 4]
        count = {1:0, 4:0}
        times = 60000
        for i in range(times):
            result = roll("C")
            self.assertTrue(result in expected, f'When calling roll("C") result must be 1 or 4, now result was {result}')
            count[result] += 1

        n = 1
        m = 1
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("C") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

        n = 4
        m = 5
        self.assertTrue(m*9700 < count[n] < m*10300, f'When calling roll("C") {times} times, number {n} should be the result approx {m*times//6} times, now it was thrown {count[n]} times, your dice cannot work properly!')

    def test_3_function_play_exists_and_return_value_is_correct(self):
        try:
             from src.dice_roller import play
        except:
            self.assertTrue(False, f'Your code should contain function named as play(die1: str, die2: str, times: int)')
        
        try:
            result = play("A", "B", 10)
        except:
            self.assertTrue(False, f'Make sure, that following function call works play("A", "B", 10)')

        try:
            result = play("C", "A", 10)
        except:
            self.assertTrue(False, f'Make sure, that following function call works play("C", "A", 10)')

        try:
            result = play("B", "C", 10)
        except:
            self.assertTrue(False, f'Make sure, that following function call works play("B", "C", 10)')        

        self.assertTrue(type(result) == tuple, f'Function play is expected to return a tuple, which contains three integers, when executing the following code play("B", "C", 10).\nThe function returned {result}')
        self.assertTrue(len(result)  == 3, f'Function play is expected to return a tuple, which contains three integers, when executing the following code play("B", "C", 10).\nThe function returned {result}')
        self.assertTrue(type(result[0]) == int, f'Function play is expected to return a tuple, which contains three integers, when executing the following code play("B", "C", 10).\nThe function returned {result}')
        self.assertTrue(type(result[1]) == int, f'Function play is expected to return a tuple, which contains three integers, when executing the following code play("B", "C", 10).\nThe function returned {result}')
        self.assertTrue(type(result[2]) == int, f'Function play is expected to return a tuple, which contains three integers, when executing the following code play("B", "C", 10).\nThe function returned {result}')

    def test_4_return_values_make_sense(self):
        from src.dice_roller import play
        n1 = "A"
        n2 = "B"
        code = f'play("{n1}", "{n2}", 100)'
        result = play(n1, n2, 100)
       
        self.assertEqual(result[0] + result[1] , 100, f'When calling {code} sum of the wins must be 100, now the return value was {result}')
        self.assertTrue(result[0] > 0 and result[1] > 0, f'When calling {code} both of must have wins, now the return value was {result}')
        self.assertTrue(result[2] == 0, f'When calling {code} the result cannot include ties, the return value was {result}')

        n1 = "C"
        n2 = "A"
        code = f'play("{n1}", "{n2}", 100)'
        result = play(n1, n2, 100)
       
        self.assertEqual(result[0] + result[1] , 100, f'When calling {code} sum of the wins must be 100, now the return value was {result}')
        self.assertTrue(result[0] > 0 and result[1] > 0, f'When calling {code} both of must have wins, now the return value was {result}')
        self.assertTrue(result[2] == 0, f'When calling {code} the result cannot include ties, the return value was {result}')

        n1 = "B"
        n2 = "C"
        code = f'play("{n1}", "{n2}", 100)'
        result = play(n1, n2, 100)
       
        self.assertEqual(result[0] + result[1] , 100, f'When calling {code} sum of the wins must be 100, now the return value was {result}')
        self.assertTrue(result[0] > 0 and result[1] > 0, f'When calling {code} both of must have wins, now the return value was {result}')
        self.assertTrue(result[2] == 0, f'When calling {code} the result cannot include ties, the return value was {result}')

        n1 = "C"
        n2 = "C"
        code = f'play("{n1}", "{n2}", 1000)'
        result = play(n1, n2, 1000)
       
        self.assertEqual(result[0] + result[1] + result[2], 1000, f'When calling {code} sum of the wins must be 100, now the return value was {result}')
        self.assertTrue(result[0] > 0 and result[1] > 0, f'When calling {code} both of must have wins, now the return value was {result}')
        self.assertTrue(result[2] > 0, f'When calling {code} the result must have ties, the return value was {result}')


    def test_5_A_against_B(self):
        from src.dice_roller import play

        wons = { "A":0, "B":0, "C": 0}
        times = 100
        for i in range(times):
            n1 = "A"
            n2 = "B"
            result = play(n1, n2, 100)
            code = f'play("{n1}", "{n2}", 100)'
            wons[n1] += result[0]
            wons[n2] += result[1] 
        self.assertTrue(wons[n1] > wons[n2], f'When calling {times} times {code} dice {n1} is expected to win more often')

    def test_5_B_against_C(self):
        from src.dice_roller import play

        wons = { "A":0, "B":0, "C": 0}
        times = 100
        for i in range(times):
            n1 = "B"
            n2 = "C"
            result = play(n1, n2, 100)
            code = f'play("{n1}", "{n2}", 100)'
            wons[n1] += result[0]
            wons[n2] += result[1] 
        self.assertTrue(wons[n1] > wons[n2], f'When calling {times} times {code} dice {n1} is expected to win more often')

    def test_5_C_against_A(self):
        from src.dice_roller import play

        wons = { "A":0, "B":0, "C": 0}
        times = 100
        for i in range(times):
            n1 = "C"
            n2 = "A"
            result = play(n1, n2, 100)
            code = f'play("{n1}", "{n2}", 100)'
            wons[n1] += result[0]
            wons[n2] += result[1] 
        self.assertTrue(wons[n1] > wons[n2], f'When calling {times} times {code} dice {n1} is expected to win more often')

if __name__ == '__main__':
    unittest.main()