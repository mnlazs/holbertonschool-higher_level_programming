#!/usr/bin/python3
"""
    Funcion que retorna una representacion de Json
"""


import json
"""
    Importacion de un modulo que retorna la representacion
    """
 

def to_json_string(my_obj):
    return json.dumps(my_obj)
