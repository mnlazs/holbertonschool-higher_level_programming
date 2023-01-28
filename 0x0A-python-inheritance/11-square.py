#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(self.__size, self.__size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
