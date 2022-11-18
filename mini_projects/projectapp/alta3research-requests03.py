#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/inventory"

new_product= {
           "item": "television",
           "brand": "LG",
           "price": 500
          }

# json.dumps takes a python object and returns it as a JSON string
new_product= json.dumps(new_product)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json= new_product)

# pretty-print the response back from our POST request
pprint(resp.json())