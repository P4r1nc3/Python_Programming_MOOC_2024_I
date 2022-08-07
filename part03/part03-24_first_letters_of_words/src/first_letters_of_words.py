# Write your solution here
sentence = input("Please type in a sentence: ")

i = 0
if len(sentence) != 0:
    print(sentence[0])
    while i < len(sentence):
        if sentence[i] == " ":
            print(sentence[i+1])
        i += 1