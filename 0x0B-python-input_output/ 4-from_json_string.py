#!/usr/bin/python3
"""
    Return an obj represented by a JSON string
""""

import json


def from_json_string(my_str):
    """ Return an obj represented by a JSON string
    """
    
    return json.loads(my_str)