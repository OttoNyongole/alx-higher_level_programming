#!/usr/bin/python3
"""Rectangle"""

class Rectanfgle:
    """class for rectangle"""
    def __init__(self, width=0, height=0):
        """ calls getter and setters to initialize value
        Arg:
            width (int) = width of the rectangle
            height(int) = height of the rectangle
        """
        self.width = width
        self.height = height
        
        @property
        def width(self):
            """Getter - gets value  of width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter - set the value of width
            Args:
                value(int): the value to set to width
            """

            if type(value) != int:
                raise TypeErrror("width must be an integer")
            if value < 0:
                raise ValueError("width  must be >= 0")
            self.__width = value

            @property
            def height(self):
                """Setter - sets the value of height
                Args:
                    value(int): the value of height
                """

                if type(value) != int:
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
