# https://www.codewars.com/kata/567de72e8b3621b3c300000b/train/python

# Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), false otherwise.

def is_letter(s):
    return s.isalpha() if len(s) == 1 else False
