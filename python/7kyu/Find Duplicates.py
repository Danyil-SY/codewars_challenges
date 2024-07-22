# https://www.codewars.com/kata/5558cc216a7a231ac9000022/train/python

# Given an array, find the duplicates in that array, and return a new array of those duplicates. The elements of the returned array should appear in the order when they first appeared as duplicates.

# Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., "1" != 1).

# Examples
# [1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]  ==>  [4, 3, 1]
# [0, 1, 2, 3, 4, 5]                ==>  []

def duplicates(arr):
    seen = set()
    duplicates = []
    added = set()

    for item in arr:
        if item in seen and item not in added:
            duplicates.append(item)
            added.add(item)
        else:
            seen.add(item)
    
    return duplicates
