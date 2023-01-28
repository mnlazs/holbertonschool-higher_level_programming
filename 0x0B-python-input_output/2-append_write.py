#!/usr/bin/python3
""""
Funcion que el numero de caracteres agregados
"""


def append_write(filename="", text=""):
    """
utiliza append funtion para agregar texto al final de archivo
"""

    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)
        return num_chars
