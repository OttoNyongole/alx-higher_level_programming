#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("99", end='\n')
    else:
        print("{0:0=2d}, ".format(n), end='')