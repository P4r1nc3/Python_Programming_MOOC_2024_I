# Write your solution here
wage = float(input("Hourly wages:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")

payment = wage * hours
if day == "Sunday":
    payment *= 2
print(f"Daily wages: {payment} euros")