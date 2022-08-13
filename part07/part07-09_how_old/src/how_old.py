# Write your solution here
from datetime import datetime

from datetime import datetime

def calculate_age(year: int, month: int, day: int):
    birthday = datetime(year, month, day)
    millenium = datetime(1999, 12, 31)
    difference = millenium - birthday
    return difference.days

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

age_by_millenium = calculate_age(year, month, day)
if age_by_millenium > 0:
    print(f'You were {age_by_millenium} days old on the eve of the new millennium.')
else:
    print(f"You weren't born yet on the eve of the new millennium.")