# Write your solution here
def shortest(my_list : list):
    shortest = my_list[0]
    for i in my_list:
        if len(i) <= len(shortest):
            shortest = i
    return shortest
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)