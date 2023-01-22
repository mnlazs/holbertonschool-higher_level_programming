#!/usr/bin/python3
"""
    Modulo Comments
"""


def say_my_name(first_name, last_name=""):
    """ print my first and last name """
    str_error = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(str_error)
    print("My name is", first_name, last_name)
