# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = 0

while i < len(word)-2:
    if word[i] == char:
        print(word[i:i+3])
        break
    i += 1
