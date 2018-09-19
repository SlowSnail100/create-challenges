#!/usr/bin/python
import string
import random

# a function to generate number plate
def generateplate():
    alphabet = string.ascii_uppercase.replace("I","").replace("Q","") # create alphabet and remove the letter I
    print("{ab}{num}{xyz}".format(ab=''.join(random.choice(alphabet) for x in range(2)),num=format(random.choice(list(range(2,20))+list(range(51,70))),'02'),xyz=''.join(random.choice(alphabet) for x in range(3))))

if __name__ == "__main__":
    generateplate()
