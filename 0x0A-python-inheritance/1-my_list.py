#!/usr/bin/python3
"""
class MyList inherits class list
"""


class MyList(list):
    """child class of class list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))


