#!/usr/bin/python3
"""
Funcion que lee un archivo de texto
"""


def read_file(filename=""):
    """
Funcion que lee un archivo de texto
"""

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
