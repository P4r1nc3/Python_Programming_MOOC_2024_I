import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        persons = json.loads(data)
        for person in persons:
            name = person['name']
            age = str(person['age']) + ' years'
            hobbies = '(' + ', '.join(person['hobbies']) + ')'
            print(f'{name} {age} {hobbies}')