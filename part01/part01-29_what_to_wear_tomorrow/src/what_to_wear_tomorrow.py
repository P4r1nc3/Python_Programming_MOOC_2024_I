# Write your solution here
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it raine (yes/no):")
print("Wear jeans and a T-shirt")

if temp < 21:
    print("I recommend a jumper as well")

if temp < 11:
    print("I recommend a jumper as well")
    print("Take a jacket with you")

if temp < 6:  
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")