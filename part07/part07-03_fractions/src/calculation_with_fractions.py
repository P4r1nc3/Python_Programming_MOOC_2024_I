# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    fractions = []
    for i in range(amount):
        fractions.append(Fraction(1, amount))
    return fractions

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()
    print(fractionate(5))