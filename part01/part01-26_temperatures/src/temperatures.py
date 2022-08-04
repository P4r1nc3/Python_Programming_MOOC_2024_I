# Write your solution here
num = int(input("Please type in a temperature (F):"))
celsius = (num - 32) * 5.0/9.0
print(f"{num} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")