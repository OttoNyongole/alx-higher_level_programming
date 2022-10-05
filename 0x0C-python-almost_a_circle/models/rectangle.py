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
        _display = ''

        _display += "\n" * self.y
        for i in range(self.height):
            _display += (" " * self.x) + (self.width * "#")
            if i != self.height - 1:
                _display += '\n'
        print(_display)

    def update(self, *args, **kwargs):
        """
        update method
        Args:
            *args:
                pointer to an array of data
        """
        if args and len(args):
            for idx, arg in enumerate(args):
                if idx == 0:
                    super().__init__(arg)
                if idx == 1:
                    self.id = arg
                if idx == 2:
                    self.width = arg
                if idx == 3:
                    self.height = arg
                if idx == 4:
                    self.x = arg
                if idx == 5:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
    def to_dictionary(self):
        """to_dictionary method
        Return:
            return the dictionary representation of a Rectangle.
            this dictionary must contain:
             - id
             - width
             - height
             - x
             - y
        """
        attrs_list = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attrs_list}


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
