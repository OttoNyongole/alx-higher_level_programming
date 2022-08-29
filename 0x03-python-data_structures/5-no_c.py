#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        for char in list(my_string):
            if char == 'c' or char == 'C':
                my_string.revove(char)
        return my_string
