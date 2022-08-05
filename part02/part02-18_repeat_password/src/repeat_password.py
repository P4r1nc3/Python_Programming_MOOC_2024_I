# Write your solution here
password1 = input("Password: ")

while True:
    password2 = input("Repeat password: ")

    if password1 != password2:
        print("They do not match!")
    else:
        break
print("User account created!")