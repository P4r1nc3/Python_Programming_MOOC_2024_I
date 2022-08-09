# Write your solution here
def same_chars(text, int1, int2):
    if int1 >= len(text) or int2 >= len(text):
        return False
    return text[int1] == text[int2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 1, 3))
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))