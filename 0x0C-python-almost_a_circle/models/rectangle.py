#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base



class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def area(self):
            """Returns the area of the rectangle"""
            return self.width * self.height

    def display(self):
        """Display character # in stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print('#', end="") for j in range(self.width)]
            print()


    def __init__(self, width, height, x=0, y=0, id=None):
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

        @width.setter
        def width(self, value):
            """sets the value to the width"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """get the value of height"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the value to the height"""
            if type(value) != int:
                raise TypeError("height must be an integer")

            if value <= 0:
                raise ValueError("height must be > 0")

            self.__height = value

        @property
        def x(self):
            """get the value of x """
            return self.__x

        @x.setter
        def x(self, value):
            """sets the value to x """
            
            if type(value) != int:
                raise TypeError("x must be an integer")

            if value < 0:
                raise ValueError("x must be >= 0")

            self.__x = value


        @property
        def y(self):
            """get the value of y"""
            return self.__y

        @y.setter
        def y(self, value):
            """sets the value to y"""
            if type(value) != int:
                raise TypeError("y must be an integer")

            if value < 0:
                raise ValueError("y must be >= 0")

            self.__y = value

        def __str__(self):
            """Override str method from Base"""
            return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y, self.width, self.height)
