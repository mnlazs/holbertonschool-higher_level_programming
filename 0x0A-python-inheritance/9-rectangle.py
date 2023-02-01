#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry.
   Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
   Public instance method:\
   def integer_validator(self, name, value):\
   that validates value
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self): \
           that raises an Exception with\
           the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:\
           def integer_validator(self, name, value):\
           that validates value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height: \
        def __init__(self, width, height)
        width and height must be positive integers,\
        validated by integer_validator"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the following rectangle description:\
        [Rectangle] <width>/<height>"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
