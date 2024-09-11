# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python

# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

# Good luck!

import re
def solve(s):
    matches = re.findall('[aeiou]+', s)
    return max(list(map(len, matches))) if s else 0
