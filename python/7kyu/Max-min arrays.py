# https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

# In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first max value is followed by the first minimum, followed by second max value then second min value, etc.

# For example:

# solve([15,11,10,7,12]) = [15,7,12,10,11]
# The first max is 15 and the first min is 7. The second max is 12 and the second min is 10 and so on.

# More examples in the test cases.

# Good luck!

def solve(arr):
    max_sorted = sorted(arr, reverse=True)
    min_sorted = sorted(arr)
    result = []
    
    for i in range(len(arr) // 2 + 1):
        if i < len(max_sorted):
            result.append(max_sorted[i])
        if i < len(min_sorted):
            result.append(min_sorted[i])
            
    return result[:len(arr)]
