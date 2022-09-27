#!/usr/bin/python3
"""The module"""
def inherits_from(obj, a_class):
    """
    checks if its a subclass
    Args:
        obj = The objects to check
        a_class = The class to match if its inherited from

    Return: 
            True if the object is axactly a subclass otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
