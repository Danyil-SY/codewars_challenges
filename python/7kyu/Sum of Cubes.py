# see description here:
# https://www.codewars.com/kata/59a8570b570190d313000037/train/python

# Write a function that takes a positive integer n, sums all the cubed values from 1 to n (inclusive), and returns that sum.

# Assume that the input n will always be a positive integer.

# Examples: (Input --> output)

# 2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
# 3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)

def sum_cubes(n):
    return sum(x ** 3 for x in range(1, n+1))
