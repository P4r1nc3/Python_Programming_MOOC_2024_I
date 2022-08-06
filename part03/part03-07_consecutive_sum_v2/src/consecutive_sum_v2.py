# Write your solution here
limit = int(input("Limit:"))
num = 1
value = 1
x = "1"
while value < limit:
    num += 1
    value += num
    x += f" + {num}"
print(f"The consecutive sum: {x} = {value}")