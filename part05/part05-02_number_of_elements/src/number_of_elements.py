# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    counter = 0
    for i in range(len(my_matrix)): # using the number of rows in the matrix
        for j in range(len(my_matrix[i])): # using the number of items on each row 
            if my_matrix[i][j] == element:
                counter += 1
    return counter
    
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))