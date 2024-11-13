# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

# Your job is to implement a function which returns the last D digits of an integer N as a list.

# Special cases:
# If D > (the number of digits of N), return all the digits.
# If D <= 0, return an empty list.
# Examples:
# N = 1
# D = 1
# result = [1]

# N = 1234
# D = 2
# result = [3, 4]

# N = 637547
# D = 6
# result = [6, 3, 7, 5, 4, 7]

def solution(n,d):
    str_n = str(n)
    
    if d > 0:
        return [int(digit) for digit in str_n[-d:]]
    
    return []
