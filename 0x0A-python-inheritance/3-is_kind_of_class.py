#!/usr/bin/python3
"""
    Get if a object is exactly an instance of the \
    specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object if an instance of\
       exactly an instance of the specified class \
       ; otherwise False"""

    if isinstance(obj, a_class):
        return True
    if hasattr(obj, '__class__') and issubclass(obj.__class__, a_class):
        return True
    return False
