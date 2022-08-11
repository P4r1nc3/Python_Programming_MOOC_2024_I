# write your solution here
def put_file_lines_in_list(file_name):
    with open(file_name) as file:
        file_as_list = []
        for line in file:
            line = line.replace('\n', '')
            file_as_list.append(line)
    return file_as_list

def main():
    text = input('Write text: ')
    text_list = text.split(' ')
    all_words = put_file_lines_in_list('wordlist.txt')
    for index, word in enumerate(all_words):
        all_words[index] = word.lower()
    output = ''
    for text in text_list:
        if text.lower() in all_words:
            output += text
        else:
            output += '*' + text + '*'
        output += ' '
    print(output)

main()