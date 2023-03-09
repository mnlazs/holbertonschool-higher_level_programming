#!/usr/bin/python3
"""ERROR"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
