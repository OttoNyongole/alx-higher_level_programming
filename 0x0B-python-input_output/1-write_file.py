#!/usr/bin/python3
"""
Module for returning number of lines in text file
"""


def write_file(filename="", text=""):
    """uses open() and write() to write string to a text file.
    Return:
        no of characters read
    Args:
        filename: text file to write into
        text (str): string to write to text file
    """
    with open(filename, 'w', encoding='utf8') as file:
        return file.write(text)
