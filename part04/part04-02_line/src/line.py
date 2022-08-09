# Write your solution here
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")