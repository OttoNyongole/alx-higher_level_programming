#!/usr/bin/python3
#A function to print elements in a list using format() function
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
