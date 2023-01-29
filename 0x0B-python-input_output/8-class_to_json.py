#!/usr/bin/python3
"""
    8-from_json_string.py
    Function that writes an Object to \
    a text file, using a JSON representation.
"""


def class_to_json(obj):
    """Function that writes an Object to \
    a text file, using a JSON representation."""
    return obj.__dict__
