#!/usr/bin/python3
"""defines a class rectangle that inherits from class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Basegeometry):
    """inheriting from BaseGeometry"""

    def__init__(self, width, height):
        """
        initialize new Rectangle.
        Args:
            width (int): the width of the rectangle.
            Height (int): the height of the rectangle.
        """

        self.integer_validator("width", width)
        self.__wisth = width
        self.integer_validator("height", height)
        self.__height = height
