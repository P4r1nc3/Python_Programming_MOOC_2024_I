# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
    found_words = []
    with open('words.txt') as word_file:
        for line in word_file:
            word = line.replace('\n', '')
            if word.startswith(beginning):
                found_words.append(word)

    if len(found_words) < n:
        raise ValueError(f'Could not find {n} words that start with {beginning}. Only found {len(found_words)} words.')
    
    return sample(found_words, n)

if __name__ == "__main__":
    word_list = words(3, "ty")
    for word in word_list:
        print(word)