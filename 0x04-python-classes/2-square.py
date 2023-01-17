#!/usr/bin/python3
"""Square Class"""


class Square
"""defines class and
instantiates private instance"""

    def __inti__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must b an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        return self.__size ** 2
