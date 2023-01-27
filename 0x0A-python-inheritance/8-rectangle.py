#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry.
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self)"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:\
           def integer_validator(self, name, value):\
           that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseException):
    """Class Rentacle that inherits from BaseException"""
    def __init__(self, width, height):
        """Instantiation with width and height: \
        def __init__(self, width, height)
        width and height must be positive integers,\
        validated by integer_validator"""

        self.integer_validator("widht", width)
        self.__width = width
        self.__integer_validator("height", height)
        self.__height = height
