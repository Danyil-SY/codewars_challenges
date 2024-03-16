# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

# Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
# --the order is: uppercase letters, lowercase, numbers and special characters.
# More examples in the test cases.

def solve(s):
    uppercase, lowercase, numbers, special_chars = 0, 0, 0, 0
    for el in s:
        if el.isupper():
            uppercase += 1
        elif el.islower():
            lowercase += 1
        elif el.isdigit():
            numbers += 1
        else:
            special_chars += 1
    return [uppercase, lowercase, numbers, special_chars]
