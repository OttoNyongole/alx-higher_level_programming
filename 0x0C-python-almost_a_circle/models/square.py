#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, id, x, y)

    def __str__(self):
        """overloading method """
        prnt = "[Square] ({}) {}/{} - {}"
        return prnt.format(self.id, self.x, self.y, self.width)
