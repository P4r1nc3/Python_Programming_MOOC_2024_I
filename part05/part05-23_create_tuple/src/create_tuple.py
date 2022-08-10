# Write your solution here
def create_tuple(x: int, y: int, z: int):
    my_list = [x, y, z]

    smallest = min(my_list)
    greatest = max(my_list)
     
    tuple = (smallest, greatest, sum(my_list))

    return tuple


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))