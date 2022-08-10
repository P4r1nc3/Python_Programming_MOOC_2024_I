# Write your solution here
def invert(dictionary: dict):
    temp = {}
    
    for key, value in dictionary.items():
        temp[value] = key

    dictionary.clear()

    for key, value in temp.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print(s)