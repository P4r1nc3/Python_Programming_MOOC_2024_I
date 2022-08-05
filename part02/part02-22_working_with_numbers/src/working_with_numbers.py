# Write your solution here
count = 0
sum = 0
positive = 0
negative = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    count += 1
    print(f"Numbers typed in {count}")
    sum += num
    print(f"The sum of the numbers is {sum}")
    mean = sum / count
    print(f"The mean of the numbers is {mean}")
    if num > 0:
        positive += 1
    else:
        negative += 1
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")  
