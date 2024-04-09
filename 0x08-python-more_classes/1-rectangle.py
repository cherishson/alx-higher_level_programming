#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Rectangle class

        """
    def __init__(self, width=0, height=0):
        """
            init Rectangle class

            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            getter

            """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter

            """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
            height getter

            """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter

            """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
