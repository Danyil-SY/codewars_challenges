# https://www.codewars.com/kata/57a386117cb1f31890000039/train/python

# Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.

def parse_float(string):
    try:
        return float(string)
    except:
        return None
