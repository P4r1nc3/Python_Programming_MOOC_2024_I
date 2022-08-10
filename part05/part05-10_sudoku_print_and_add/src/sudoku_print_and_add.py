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
        
        for newCol in range(9):
            print(newDoku[newRow][newCol], end=" ")
            if (newCol + 1) % 3 == 0:
                print(end=" ")

        print()



def add_number(sudoku: list, row_no: int, column_no: int, number: int):

    sudoku[row_no][column_no] = number

    return sudoku

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)