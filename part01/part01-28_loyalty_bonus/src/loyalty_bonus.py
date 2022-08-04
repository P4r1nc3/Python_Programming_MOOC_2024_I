# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    value = points * 1.1
    print("Your bonus is 10 %")
if points >= 100:
    value = points * 1.15
    print("Your bonus is 15 %")
print(f"You now have {value} points")