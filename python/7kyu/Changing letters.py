# https://www.codewars.com/kata/5831c204a31721e2ae000294/train/python

# When provided with a String, capitalize all vowels

# For example:

# Input : "Hello World!"

# Output : "HEllO WOrld!"

# Note: Y is not a vowel in this kata.

def swap(text):
    vowels = 'aeiouAEIOU'
    return ''.join([s.upper() if s in vowels else s for s in text])
