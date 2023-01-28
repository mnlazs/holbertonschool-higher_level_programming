#!/usr/bin/python3
"""Funcion que escribe una cadena de texto
"""


def write_file(filename="", text=""):
    """Funcion que mira una cadena de texto if si no existe
crea una.
"""

    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
