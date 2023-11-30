#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Class from which rectangle objects can be instantiated"""
    def __init__(self, width=0, height=0):
        """On instantiation, gives the rectangle object a width
        and height
        Args:
            width (int, optional): the width of the rectangle object
            height (int, optional): the height of the rectangle object
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value (int): the new width of the of the rectangle object
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            value (int): the new height of the rectangle object
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle object
        Returns:
            the area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle object
        Returns:
            the perimeter of the rectangle
        """
        if (self.width == 0) or (self.height == 0):
            return 0
        return (2 * (self.width + self.height))