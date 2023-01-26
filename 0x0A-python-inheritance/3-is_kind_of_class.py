#!/usr/bin/python3
"""
    Get if a object is exactly an instance of the \
    specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object if an instance of\
       exactly an instance of the specified class \
       ; otherwise False"""
    return isinstance(obj, a_class) or
(hasattr(obj, '__class__') and issubclass(obj.__class__, a_class))
