# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
 
    return sorted(numbers)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
