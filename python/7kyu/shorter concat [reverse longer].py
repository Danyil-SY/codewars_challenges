# https://www.codewars.com/kata/54557d61126a00423b000a45/train/python

# Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

# In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

# Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
# If a and b have the same length treat a as the longer producing b+reverse(a)+b

def shorter_reverse_longer(a,b):
    len_a = len(a)
    len_b = len(b)
    
    if len_a < len_b:
        return a + b[::-1] + a
    else:
        return b + a[::-1] + b
