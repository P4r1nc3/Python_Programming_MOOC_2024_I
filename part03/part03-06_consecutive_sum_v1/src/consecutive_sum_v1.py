# Write your solution here
limit = int(input("Limit:"))
num = 1
i = 1
while i < limit:
    num += 1
    i += num
print(i)