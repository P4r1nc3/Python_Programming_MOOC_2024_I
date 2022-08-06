# Write your solution here
word = input("Please type in a string: ")
i = -1
sum = ""
while i >= -len(word):
    sum = word[i] + sum
    print(sum)
    i -= 1