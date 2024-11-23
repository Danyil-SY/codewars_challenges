# https://www.codewars.com/kata/55dc4520094bbaf50e0000cb/train/python

# Wilson primes satisfy the following condition. Let P represent a prime number.

# Then,

# ((P-1)! + 1) / (P * P)
# should give a whole number.

# Your task is to create a function that returns true if the given number is a Wilson prime.

import math

def am_i_wilson(n):
    if n <= 2:
        return False
    return ((math.factorial(n - 1) + 1) % (n ** 2)) == 0

# OR

def am_i_wilson(n):
    return n in {5, 13, 563}
