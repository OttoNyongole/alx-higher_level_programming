#!/usr/bin/python3
"""Defining the BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """NULL"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value as follows
            Args:
            name (str): name f param.
            value (int): param to check.
        Raises:
            TypeError: If value not int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")

