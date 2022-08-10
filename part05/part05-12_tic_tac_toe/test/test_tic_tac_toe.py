import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.tic_tac_toe'
function = 'play_turn'

def get_correct(test_case: list) -> int:
    pass

def get_test_case(x: int, y: int, sign = ""):
    board = [['','',''],['','',''],['','','']]
    for i in range(randint(3,8)):
        board[randint(0,2)][randint(0,2)] = choice(('X','O'))
        
    if 0<=x<=2 and 0<=y<=2:
        board[y][x] = sign
    return board 

def kopy(b):
    c = []
    for r in b:
        c.append(r[:])
    return c

@points('5.tic_tac_toe')
class TicTacToeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message =  """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.tic_tac_toe import play_turn
        except:
            self.assertTrue(False, "Your code should contain function named as play_turn(game_board: list, x: int, y: int, piece: str)")
        try:
            play_turn = load(exercise, function, 'en')
            play_turn([['','',''],['','',''],['','','']], 0, 0, 'X')
        except:
            self.assertTrue(False, "Make sure, that function can be called as follows\nplay_turn([['','',''],['','',''],['','','']], 0, 0, 'X')")

    def test_2_type_of_return_value(self):
        play_turn = load(exercise, function, 'en')
        val = play_turn([['','',''],['','',''],['','','']], 0, 0, 'X')
        self.assertTrue(type(val) == bool, f"Function {function} does not return boolean type with parameter values [['','',''],['','',''],['','','']], 0, 0, 'X'.")
    
    def test_3_free_squares(self):
        test_cases = ((0,0,"X"), (1,1,"O"), (2,2,"X"), (0,1,"X"), (1,0,"O"), (1,2,"X"), (2,1,"O"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                play_turn = load(exercise, function, 'en')

                test_board = get_test_case(test_case[0], test_case[1], "")
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)

                board_after[test_case[1]][test_case[0]] = test_case[2]
                correct = True

                test_result = play_turn(test_board, test_case[0], test_case[1], test_case[2])

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"State of the matrice\n{test_board}\ndoes not match with the model solution\n{board_after}\nwhen the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

    def test_4_reserved_squares(self):
        test_cases = ((0,0,"X"), (1,1,"O"), (2,2,"X"), (0,1,"X"), (1,0,"O"), (1,2,"X"), (2,1,"O"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_at_start = get_stdout()
                play_turn = load(exercise, function, 'en')

                test_board = get_test_case(test_case[0], test_case[1], test_case[2])
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)
                correct = False

                try:
                    test_result = play_turn(test_board, test_case[0], test_case[1], test_case[2])
                except:
                    self.assertTrue(False, f"Make sure, that you can call the function with following parameters\n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"State of the matrice\n{test_board}\ndoes not match with the model solution\n{board_after}\nwhen the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

    def test_5_invalid_squares(self):
        test_cases = ((3,0,"X"), (1,11,"O"), (2,-1,"X"), (1,3,"X"), (-1,1,"X"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                play_turn = load(exercise, function, 'en')

                test_board = get_test_case(test_case[0], test_case[1], test_case[2])
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)
                correct = False

                try:
                    test_result = play_turn(test_board, test_case[0], test_case[1], test_case[2])
                except:
                    self.assertFalse(True, f"Make sure that the function can be called with following parameters\n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

                self.assertEqual(correct, test_result, f"The result {test_result} does not match with the model solution {correct} when the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"State of the matrice\n{test_board}\ndoes not match with the model solution\n{board_after}\nwhen the parameters are \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

if __name__ == '__main__':
    unittest.main()