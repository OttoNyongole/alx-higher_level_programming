#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of the number is {}".format(number))
if number > 5:
    print("is {} and is greater than 5".format(number))
elif number == 0:
    print("is {} and is Zero".format(number))

