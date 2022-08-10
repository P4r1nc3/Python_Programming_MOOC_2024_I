# Write your solution here
def row_correct(sudoku : list, row_index : int):
    new_list = []
    for i in range(0, 9):
        sudoku[row_index][i]
        if sudoku[row_index][i] > 0 and  sudoku[row_index][i] in new_list:
            return False
        else:
            new_list.append(sudoku[row_index][i])
        
    return True




if __name__ == "__main__":

    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))