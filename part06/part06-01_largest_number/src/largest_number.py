# write your solution here
def largest():
    numbers = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            numbers.append(int(line))
    if len(numbers) > 0:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest

if __name__ == "__main__":
    largest()