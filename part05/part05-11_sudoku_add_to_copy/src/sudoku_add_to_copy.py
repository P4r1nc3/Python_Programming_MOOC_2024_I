# Write your solution here
def print_sudoku(sudoku: list):
    newRow = 0
    newCol = 0

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                sudoku[r][c] = "_"

    newDoku = sudoku[:]


    for newRow in range(9):
        if newRow > 0 and newRow % 3 == 0:
            print()
        
        for newCol in range(0,9):
            print(newDoku[newRow][newCol], end=" ")
            if (newCol + 1) % 3 == 0:
                print(end=" ")
        print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    outputSudoku = []

    for row in sudoku:
        temp = []
        for cell in row:
            temp.append(cell)
        outputSudoku.append(temp)
    outputSudoku[row_no][column_no] = number
    return outputSudoku

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    grid_copy = copy_and_add(sudoku, 1, 1, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)