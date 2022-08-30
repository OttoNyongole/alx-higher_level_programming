#!/usr/bin/python3
def max_integer(my_list=[]):
    if leng(my_list) < 0:
        return None
    else:
        sortedlist = my_list.sort()
        return sortedlist[-1]
