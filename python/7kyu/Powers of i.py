# https://www.codewars.com/kata/5a97387e5ee396e70a00016d/train/python

# i is the imaginary unit, it is defined by 
# i
# ²
# =
# −
# 1
# i²=−1, therefore it is a solution to 
# x
# ²
# +
# 1
# =
# 0
# x²+1=0.

# Your Task
# Complete the function pofi that returns 
# i
# i to the power of a given non-negative integer in its simplest form, as a string (answer may contain 
# i
# i).

def pofi(n):
    if n % 4 == 0:
        return "1"
    elif n % 4 == 1:
        return "i"
    elif n % 4 == 2:
        return "-1"
    elif n % 4 == 3:
        return "-i"