#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/inventory"

res= requests.get(URL).json()

# pretty-print the response back from our GET request
pprint(res)