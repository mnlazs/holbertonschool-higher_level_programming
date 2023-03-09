#!/usr/bin/python3
"""se importa el modulo para el uso del URL
    """

import urllib.request
with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    html = response.read()
