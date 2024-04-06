# https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python

# Compare two strings by comparing the sum of their values (ASCII character code).

# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.

# Examples:
# "AD", "BC"  -> equal
# "AD", "DD"  -> not equal
# "gf", "FG"  -> equal
# "zz1", ""   -> equal (both are considered empty)
# "ZzZz", "ffPFF" -> equal
# "kl", "lz"  -> not equal
# null, ""    -> equal

def compare(str1, str2):
    str1 = str1.upper() if str1 and not any(not char.isalpha() for char in str(str1)) else ""
    str2 = str2.upper() if str2 and not any(not char.isalpha() for char in str(str2)) else ""
        
    sum_str1 = sum(ord(char) for char in str1)
    sum_str2 = sum(ord(char) for char in str2)
    
    return sum_str1 == sum_str2
