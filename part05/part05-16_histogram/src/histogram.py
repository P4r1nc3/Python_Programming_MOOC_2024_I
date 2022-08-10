# Write your solution here
def histogram(word : str):
    letters = {}
    for i in word:
        if i not in letters:
            letters[i] = 0
        letters[i] += 1
    
    for key, value in letters.items():
        print(f"{key} {value*'*'}")

if __name__ == "__main__":
    histogram("statistically")