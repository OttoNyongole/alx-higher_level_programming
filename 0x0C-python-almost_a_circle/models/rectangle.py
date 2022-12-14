#!/usr/bin/python3
"""
This module contains the Class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    This Class Rectangle inherit from Base.
    """
    def area(self):
        """area method
        Return:
            area the rectangle
        """
        return self.width * self.height

    def display(self):
        """display method: print rectangle with symbol
        Return:
            none
        """
        _display = ''

        _display += "\n" * self.y
        for i in range(self.height):
            _display += (" " * self.x) + (self.width * "#")
            if i != self.height - 1:
                _display += '\n'
        print(_display)

    def update(self, *args, **kwargs):
        """update method
        Args:
            @*args: pointer to a array data
            @**kwargs: double pointer to a dictionary: key/value
        """
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super().__init__(arg)
                if idx == 1:
                    self.width = arg
                if idx == 2:
                    self.height = arg
                if idx == 3:
                    self.x = arg
                if idx == 4:
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
        """
        init method
        Args:
            @width: width rectangle.
            @height: height rectangle.
            @x: x position
            @y: y position
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width
        Attributes:
            @__width: rectangle width
        Args:
            @value: rectangle width value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height
        Attributes:
            @__height: rectangle height
        Args:
            @value: rectangle height value
        """
        if type(value) != int:
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x
        Attributes:
            @__x: x position
        Args:
            @value: x position value
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter y"""
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
        """magic method __str__
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        _print = "[Rectangle] ({}) {}/{} - {}/{}"
        return _print.format(self.id, self.x, self.y, self.width, self.height)
