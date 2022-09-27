#!/usr/bin/python3
"""The module"""


def is_kind_of_class(obj, a_class):
    """checks if is an inheritance or intance of a class that inherited"""
    Agrs:
        obj = the object to check
        a_class = the class to match the type with.
    Return:
          True if the object is exactly an instance
          otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
