#!/usr/bin/python3
"""ERROR"""

if __name__ == '__main__':
    from sys import argv
    import requests

response = requests.get(url)

if response.status_code >= 400:
        print("Error code:", response.status_code)
else:
        print(response.text)
