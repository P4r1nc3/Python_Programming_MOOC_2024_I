# Write your solution here
def read_file(file_name):
    with open(file_name) as diary:
        print('Entries:')
        for line in diary:
            print(line.replace('\n', ''))
        diary.close()

def update_file(file_name, entry):
    with open(file_name, 'a') as diary:
        diary.write(entry + '\n')
        diary.close()

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice = int(input('Function: '))
    if choice == 1:
        entry = input('Diary entry: ')
        update_file('diary.txt', entry)
        print('Diary saved')
    elif choice == 2:
        read_file('diary.txt')
    elif choice == 0:
        print('Bye now!')
        break