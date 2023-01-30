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
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
