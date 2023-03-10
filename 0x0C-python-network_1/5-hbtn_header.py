#!/usr/bin/python3
"""El valor de X-Request-Id es"""
import sys
import requests

url = sys.argv[1]
response = requests.get(url)

if 'X-Request-Id' in response.headers:
    print('El valor de X-Request-Id es:', response.headers['X-Request-Id'])
else:
    print('La respuesta no tiene un encabezado X-Request-Id')
