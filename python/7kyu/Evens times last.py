# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.

# Indices in sequence start from 0.

# If the sequence is empty, you should return 0.

def even_last(numbers): 
    return sum(numbers[i] for i in range(0, len(numbers), 2)) * numbers[-1] if numbers else 0
