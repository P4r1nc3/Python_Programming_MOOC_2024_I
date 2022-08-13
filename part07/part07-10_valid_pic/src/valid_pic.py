# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    try:
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])
        X = pic[6]
        yyy = int(pic[7:10])
        z = pic[10]
        nums = pic[0:6] + pic[7:10]
        index = int(nums)%31
        control = '0123456789ABCDEFHJKLMNPRSTUVWXY'[index]

        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or X not in ('-','+','A') or z != control:
            return False
        
        century = 0
        if X == '-':
            century = 1800
        elif X == '+':
            century = 1900
        elif X == 'A':
            century = 2000
        
        dob_year = century + yy

        datetime(dob_year, mm, dd)

        return True
    except:
        return False
