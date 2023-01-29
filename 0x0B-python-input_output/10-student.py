#!/usr/bin/python3

"""
Write a class Student
"""


class Student:

    """
    that defines a student by: Public instance attributes\
first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ the method to_json, return a dictionary representation
        """
        attrib = {}
        if attrs is not None and all(isinstance(keyy, str) for keyy in attrs):
            for i, j in self.__dict__.items():
                if i in attrs:
                    attrib[i] = j

        return attrib
    return self.__dict__
