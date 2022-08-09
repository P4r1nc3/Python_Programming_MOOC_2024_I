# Write your solution here

while True:
    editor = input("Editor: ")

    if editor.lower() == "notepad" or editor.lower() == "word":
        print("awful")
    elif editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")