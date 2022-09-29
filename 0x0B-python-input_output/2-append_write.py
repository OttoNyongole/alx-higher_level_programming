#!/usr/bin/python3
"""
module to appends string to a file
wuth encoding utf8 and return number of character
"""
def append_write(filename="", text=""):
    """
    Description: appends string at of text file
    Args:
        filename: file to append string to
        text (str): string to be appended
    Return:
        number of characters added
    """
    with open(filename, 'a', encoding='utf8') as file:
        return file.write(text)
