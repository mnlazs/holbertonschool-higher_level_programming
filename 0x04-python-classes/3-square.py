#!/usr/bin/python3
""" Square Class:defines a square by : (based on 2-square.py)
"""


class Square:
    """__init__

    The __init__ method initializes the size value of the square.

    Attributes:
        size (:obj:`int`, optional): The size of the square.
        
    Raises:
        TypeError: If `size` type is not `int`.
            
        ValueError: If `size` is less than `0`.
        
    """   

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self.size ** 2

