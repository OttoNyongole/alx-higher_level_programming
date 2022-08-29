#!/usr/bin/python3
def no_c(my_string):
    list_chars = list(my_string)
    for char in list_chars:
        if char == 'c' or char == 'C':
            list_chars.remove(char)
    return("".join(list_chars))
