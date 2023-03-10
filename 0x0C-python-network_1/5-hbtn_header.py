#!/usr/bin/python3
"""
Python script for requests
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

response = requests.post(url, data={'email': email})

print(response.text)
