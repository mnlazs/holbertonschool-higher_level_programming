#!/usr/bin/python3
"""Fetches header"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
