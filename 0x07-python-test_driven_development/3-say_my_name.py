#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")
    print("My name is" + first_name + " " + last_name)