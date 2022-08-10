# Write your solution here
def factorials(n: int):
    my_dictionary = {}
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
        my_dictionary[i] = factorial

    return my_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
