#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'la_carpetica', encoding='utf-8') as file:
        print(file.read())
