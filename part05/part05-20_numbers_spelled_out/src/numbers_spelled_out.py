# Write your solution here
def dict_of_numbers():

    dictionary = {}
    numbers = []
    for initialise in range(100):
        numbers.append(initialise)

    #print(numbers)

    word0 = ['zero']
    wordints = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine']
    wordteens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wordtens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    rest = []
    
    for i in range(len(wordtens)):
        rest.append(wordtens[i])
        for j in range(len(wordints)):
            rest.append(wordtens[i] + "-" + wordints[j])
    
    wordListFinal = []
    wordListFinal.append(word0[0])
    for i in wordints:
        wordListFinal.append(i)
    for i in wordteens:
        wordListFinal.append(i)
    for i in rest:
        wordListFinal.append(i)
    #print(wordListFinal)

    dictionary = {numbers[i] : wordListFinal[i] for i in range(len(numbers))}

    return dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])