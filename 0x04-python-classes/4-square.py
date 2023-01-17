#!/usr/bin/python3
class Square:
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
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end="")
                print()

