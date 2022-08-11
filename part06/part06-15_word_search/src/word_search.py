# Write your solution here

def compare_dot(word_with_dot, word):
    same = True
    for i in range(len(word)):
        if word_with_dot[i] != '.' and word_with_dot[i] != word[i]:
            same = False
    return same

def find_words(search_term: str):
    found_terms = []

    with open('words.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            word = line.strip()
            if ('.' in search_term) and len(search_term) == len(word):
                if compare_dot(search_term, word) == True:
                    found_terms.append(word)
            elif search_term.startswith('*'):
                if word.endswith(search_term[1:]):
                    found_terms.append(word)
            elif search_term.endswith('*'):
                if word.startswith(search_term[:-1]):
                    found_terms.append(word)
            else:
                if search_term == word:
                    found_terms.append(word)

    return found_terms
    
if __name__ == "__main__":
    print(find_words('acq*'))