# Write your solution here
def squared(text, num):
    tokens = []
    k = 0
    for i in text:
        tokens += i

    for x in range(num):
        for y in range(num):
            i = tokens[k]
            print(i, end=(''))
            k += 1
            if k == len(tokens):
                k = 0
        print()



# Testing the function
if __name__ == "__main__":
    squared("text", 3)