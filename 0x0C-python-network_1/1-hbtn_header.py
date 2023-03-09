#!/usr/bin/python3
"""toma una URL como entrada, y  envíe una solicitud HTTP a esa URL 
    y muestre el valor de la variable
    """
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
