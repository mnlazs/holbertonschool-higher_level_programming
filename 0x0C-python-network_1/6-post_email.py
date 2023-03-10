#!/usr/bin/python3
"""Takes in a URL, email address, sends a POST request with email param"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

response = requests.post(url, data={'email': email})

print(response.text)
