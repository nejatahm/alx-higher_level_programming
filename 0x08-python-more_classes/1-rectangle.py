#!/usr/bin/python3
"""
Class which defines a rectangle.
"""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """set the attributes for the rectangle object.
        Args:
            width(int): the rectangle width.
            height(int) the rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of rectangle."""
        return self.width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer.")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >=0")
        else:
            raise TypeError("height must be an integer")

