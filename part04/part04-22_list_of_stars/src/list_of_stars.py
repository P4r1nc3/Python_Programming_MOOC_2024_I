# Write your solution here
def list_of_stars(list : list):
    size = len(list)
    i = 0
    while i < size:
        print("*" * list[i])
        i += 1
        
if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])