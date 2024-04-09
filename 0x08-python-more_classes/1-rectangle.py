#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Rectangle class

        Attributes:
            width(int) : private
            height(int) : private

        """
    def __init__(self, width=0, height=0):
        """
            init Rectangle class


            Args:
                width (int) : the width of the rectangle
                height (int) : the height of the rectangle
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            width getter

            Return: returns the value of the width in int

            """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter

        Args:
            value (int) : the value to set

        raises:
            TypeError : when width is not an int
            ValueError : when value is less than 0


            """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
            height getter


        Return: returns the height of the rectangle in int
            """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter

        Aregs:
            value (int) : the value to set


        raises:
            TypeError : when width is not setr
            ValueError : when value is less than 1

            """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
