#!/usr/bin/python3
class Square:
"""
A class that define a square by:
-private instance attribute: suze
-Instantiation with size (no type/value verification)
"""
    def __init__(self, size):
 """
Initialize the square with a given size
:param size: The size of the square (int or float)
"""
    self.size = size
