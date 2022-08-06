# Write your solution here
word = input("Please type in a string: ")
second = word[1]
secondLast = word[-2]

if second != secondLast:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {second}")