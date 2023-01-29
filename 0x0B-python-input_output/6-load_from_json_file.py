#!/usr/bin/python3
"""
    function that creates an Object from a “JSON file
    """
import json
"""function that creates an Object from a “JSON file
    """


def load_from_json_file(filename):
    """funtion"""

    with open(filename, 'r') as file:
        return json.load(file)
