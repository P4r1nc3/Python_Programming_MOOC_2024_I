# Write your solution here

def read_file(file_name: str) -> list:
    with open(file_name) as file:
        content = []
        for line in file:
            line = line.replace('\n','')
            line = line.split(';')
            content.append(line)
        return content

def evaluate_data(content: list, correct_file_name: str, incorrect_file_name: str):
    open(correct_file_name, 'w').close()
    open(incorrect_file_name, 'w').close()
    correct_file = open(correct_file_name, 'w')
    incorrect_file = open(incorrect_file_name, 'w')
    for solution in content:
        sol = ';'.join(solution)
        sol += '\n'
        if eval(solution[1]) == int(solution[2]):
            correct_file.write(sol)
        else:
            incorrect_file.write(sol)
    correct_file.close()
    incorrect_file.close()

def filter_solutions():
    content = read_file('solutions.csv')
    evaluate_data(content, 'correct.csv', 'incorrect.csv')
