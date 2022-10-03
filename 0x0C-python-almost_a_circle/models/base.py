#!/usr/bin/python3
"""Python Package with modules"""
class Base:
    """
    Args:
        __nb_objects = 0: arguments of the class
    Parameters:
        @id: number of id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This is init method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
