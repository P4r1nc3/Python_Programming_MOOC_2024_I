# Write your solution here
def everything_reversed(list : list):
    new_list = []
    i = len(list) - 1
    while i >= 0:
        rev_word = list[i]
        new_list.append(rev_word[::-1])
        i -= 1
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)