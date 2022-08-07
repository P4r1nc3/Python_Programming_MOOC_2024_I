def chessboard(length):
    tokens = ["0", "1"]

    for x in range(length):
        for y in range(length):
            i = tokens[(x + y + 1) % 2]
            print(i, end=(''))
        print()
    

# Testing the function
if __name__ == "__main__":
    chessboard(3)