# https://www.codewars.com/kata/5959ec605595565f5c00002b/train/python

# Write a function that reverses the bits in an integer.

# For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

# You can assume that the number is not negative.

def reverse_bits(n):
    binary_str = bin(n)[2:]
    reversed_binary = binary_str[::-1]
    return int(reversed_binary, 2)
