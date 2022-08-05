# Write your solution here
year = int(input("Year:"))
nextYear = year + 1

while True:
    if nextYear % 4 == 0 and nextYear % 100 != 0 or nextYear % 400 == 0:
        break
    nextYear += 1
print(f"The next leap year after {year} is {nextYear}")   