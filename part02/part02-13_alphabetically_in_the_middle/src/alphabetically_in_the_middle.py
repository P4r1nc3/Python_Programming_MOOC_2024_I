# Write your solution

letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")

if letter1 > letter2 > letter3 or letter1 < letter2 < letter3:
    middle = letter2
elif letter2 > letter1 > letter3 or letter2 < letter1 < letter3:
    middle = letter1
elif letter1 > letter3 > letter2 or letter1 < letter3 < letter2:
    middle = letter3
print(f"The letter in the middle is {middle}")