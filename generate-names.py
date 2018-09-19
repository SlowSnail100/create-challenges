#!/usr/bin/python
import requests
import json
import random

def generatenames():
    regions = ["england","united%20states"]  # choose a region the name is from

    response = requests.get("http://uinames.com/api/?region={}&amount=2".format(random.choice(regions))) # send a get request to name api, amount max is 500
    jdata = json.loads(response.content) # load in the json response

    for i in jdata:
        print("{first} {surname}".format(first=i['name'],surname=i['surname'])) # print the generated name - this will eventually write to a db

generatenames()
