#!/usr/bin/python3
"""modulo que determina si proviene de la inst especificada
    """


def is_same_class(obj, a_class):
    """Function that returns True if the object is
       exactly an instance of the specified class
        """
    return type(obj) is a_class
