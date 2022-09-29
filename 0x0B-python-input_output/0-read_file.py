#!/usr/bin/python3
"""define a function that reads a text file (UTF8) prints it to stdout"""

def read_file(filename=""):
    """
    reads and prints text file in UTF8 encoding.
    We have to use with statement
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
    file.close()
