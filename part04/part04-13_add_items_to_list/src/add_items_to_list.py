# Write your solution here
size = int(input("How many items: "))
list = []
i = 1 
while i <= size:
    item = int(input(f"Item {i}:"))
    list.append(item)
    i += 1
print(list)