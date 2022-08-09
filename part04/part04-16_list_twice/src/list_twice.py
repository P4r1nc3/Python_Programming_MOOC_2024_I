# Write your solution here
list = []

while True:
    number = int(input("New item: "))
    if number == 0:
        break
    list.append(number)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
print("Bye!")
