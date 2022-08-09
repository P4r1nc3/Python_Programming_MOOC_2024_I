# Write your solution here
def all_the_longest(my_list):

    longest = 0
    newList = []

    for i in my_list:
        if len(i) > longest:
            longest = len(i)

    for i in my_list:
        if len(i) == longest:
            newList.append(i)

    return newList

if __name__ == "__main__":

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)