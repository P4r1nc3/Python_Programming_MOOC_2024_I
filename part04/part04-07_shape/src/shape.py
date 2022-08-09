# Copy here code of line function from previous exercise and use it in your solution
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def shape(size1, character1, size2, chracter2):
    i = 1
    while i <= size1:
        line(i, character1)
        i += 1
    i = 1
    while i <= size2:
        line(size1, chracter2)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")