#!/usr/bin/python3
"""Module for class Rectangle"""



class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=none):
        """Construct a class Rectangle"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """get the value of width"""
            return self.__width

        """
        @width.setter
        def width(self, value):
        """
        @property
        def height(self):
            """get the value of height"""
            return self.__height

        @property
        def x(self):
            """get the value of x """
            return self.__x

        @property
        def y(self):
            """get the value of y"""
            return self.__y
