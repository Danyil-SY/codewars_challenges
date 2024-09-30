# https://www.codewars.com/kata/566044325f8fddc1c000002c/train/python

# Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".

# For example:

# "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
# "a"             --> "invalid string"

def even_chars(s): 
    if len(s) < 2 or len(s) > 100:
        return "invalid string"
    
    return [s[i] for i in range(1, len(s), 2)]
