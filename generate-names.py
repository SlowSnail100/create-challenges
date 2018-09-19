#!/usr/bin/python
import httplib
import requests

response = requests.get("http://uinames.com/api/?amount=1")
print(response.status_code)
print(response.header)
print(response.content)
