# https://www.codewars.com/kata/57b68bc7b69bfc8209000307/train/python

# Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are not allowed to use any loops (including for, for/in, while, and do/while loops).

# The array will never be empty.

def average(scores):
    return round(sum(scores) / len(scores))
