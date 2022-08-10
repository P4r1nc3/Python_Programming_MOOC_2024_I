# Write your solution here
def column_correct(list : list, column_num : int):
    new_list = []
    for i in range(len(list)): 
        for j in range(len(list[i])): 
            if list[i][column_num] > 0 and  list[i][column_num] in new_list:
                return False
        else:
            new_list.append(list[i][column_num])

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
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))    