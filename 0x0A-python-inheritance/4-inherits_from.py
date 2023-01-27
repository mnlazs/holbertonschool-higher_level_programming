#!/usr/bin/python3
"""
    This funtion get the object is an instance
    of a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):

    """ Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
