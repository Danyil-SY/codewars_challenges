# https://www.codewars.com/kata/58e43389acfd3e81d5000a88/train/python

# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.

# Write a function calculating circumference of a Circle.

# Tests round answers to 6 decimal places.

import math 

def circle_circumference(circle):
    return circle.radius * 2 * math.pi
