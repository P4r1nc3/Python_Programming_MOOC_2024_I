# Write your solution here
def is_week_valid(week: str):
    try:
        week = int(week)
        return True
    except:
        return False

def are_numbers_valid(numbers: list):
    try:
        numbers = numbers.split(',')

        if len(numbers) != 7:
            return False
        
        for num in numbers:
            number = int(num)
            if number < 1 or number > 39 or numbers.count(num) > 1:
                return False

        return True
    
    except:
        return False

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    correct_file = open('correct_numbers.csv', 'a')
    with open('lottery_numbers.csv') as lottery_file:
        for line in lottery_file:
            original_line = line
            line = line.replace('\n','')
            parts = line.split(';')
            week = parts[0].split(' ')[1]
            numbers = parts[1]
            if is_week_valid(week) and are_numbers_valid(numbers):
                correct_file.write(original_line)
    correct_file.close()