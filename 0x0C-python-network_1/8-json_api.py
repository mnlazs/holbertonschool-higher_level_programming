#!/usr/bin/python3
"""
Search API
"""

if __name__ == "__main__":
    import requests
    import sys

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

response = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data.get("id"), data.get("name")))
    else:
        print("ningún resultado")
except ValueError:
    print("No es un JSON válido")
