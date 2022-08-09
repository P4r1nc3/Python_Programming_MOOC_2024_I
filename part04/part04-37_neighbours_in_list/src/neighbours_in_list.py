# Write your solution here
def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))