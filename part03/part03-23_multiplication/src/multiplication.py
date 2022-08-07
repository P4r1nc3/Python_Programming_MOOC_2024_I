# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1