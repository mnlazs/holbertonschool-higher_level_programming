#!/usr/bin/python3
"""
Module documentation here lalala
"""


class Rectangle:
    """
    This class represents a rectangle with private instance attributes
    width and height. It has methods to set and get their values,
    and raise exceptions if their values are not integers or less than 0.
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("with must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        area = self.height * self.width
        return area
    
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        mystr = ""
        if (self.width == 0 or self.height == 0):
            return (mystr)
        mystr = (('#' * self.width)+ '\n')*(self.height -1) + ('#' * self.width)
        return mystr
    
    def __repr__(self):
        return ("Rentangle({0}, {1})".format(self.width, self.height))        