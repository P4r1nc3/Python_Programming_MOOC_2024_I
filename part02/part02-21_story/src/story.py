# Write your solution here
story = ""
last = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last:
        break
    story = story + word + " "
    last = word
print(story)

