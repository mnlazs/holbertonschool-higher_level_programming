#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry.
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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
