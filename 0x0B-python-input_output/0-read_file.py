#!/usr/bin/python3
"""
Funcion para leer un archivo
"""


def read_file(filename=""):
    """
    la funcion lee el archivo de texto e imprime su salida
    """

with open(filename, 'la_carpetica', encoding='utf-8') as file:
        print(file.read())
