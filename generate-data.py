#!/usr/bin/python
import requests
import json
import string
import random

num = 5 # number of plates and names to generate - has a max of 500.

# function to generate number plate
def generateplate(num):
    for a in xrange(num):
        alphabet = string.ascii_uppercase.replace("I","").replace("Q","") # create alphabet and remove the letter I
        print("{ab}{num}{xyz}".format(ab=''.join(random.choice(alphabet) for x in range(2)),num=format(random.choice(list(range(2,20))+list(range(51,70))),'02'),xyz=''.join(random.choice(alphabet) for x in range(3))))

# function to generate a list of random names for use
def generatenames(num):
    regions = ["england","united%20states"]  # choose a region the name is from

    response = requests.get("http://uinames.com/api/?region={r}&amount={n}".format(r = random.choice(regions), n = num)) # send a get request to name api, amount max is 500
    jdata = json.loads(response.content) # load in the json response

    for j in jdata:
        print("{first} {surname}".format(first=j['name'],surname=j['surname'])) # print the generated name - this will eventually write to a db

if __name__ == "__main__":
    generateplate(num)
    generatenames(num)
