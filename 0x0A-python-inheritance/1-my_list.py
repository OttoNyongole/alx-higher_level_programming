#!/usr/bin/python3
"""
class MyList inherits class list
"""


class MyList(list):
    """class MyList inherits the parent list"""
    def __init__(self):
        super().__init__()
    def print_sorted(self):
        print(sorted(self))


