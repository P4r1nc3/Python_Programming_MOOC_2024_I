# Write your solution here

def add_to_dict(dict_file_name: str, finnish: str, english: str):
    with open(dict_file_name, 'a') as file:
        file.write(finnish + ';' + english + '\n')
    print('Dictionary entry added')

def search_dict(dict_file_name: str, search_term: str):
    search_term = search_term.lower()
    with open(dict_file_name) as file:
        for line in file:
            line = line.replace('\n','')
            line = line.strip()
            parts = line.split(';')
            finnish = parts[0].lower()
            english = parts[1].lower()
            if search_term in finnish or search_term in english:
                print(f'{finnish} - {english}')

def main():
    dict_file_name = 'dictionary.txt'
    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        choice = int(input('Function: '))
        if choice == 1:
            finnish = input('The word in Finnish: ')
            english = input('The word in English: ')
            add_to_dict(dict_file_name, finnish, english)
        elif choice == 2:
            search_term = input('Search term: ')
            search_dict(dict_file_name, search_term)
        elif choice == 3:
            print('Bye!')
            break

main()