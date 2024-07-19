# https://www.codewars.com/kata/567bed99ee3451292c000025/train/python

# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.

def is_vowel(s):
    return s.lower() in ["a", "e", "i", "o", "u"] if len(s) > 0 else False
