# Write your solution here
factorial = 1
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")
    factorial = 1
print("Thanks and bye!")