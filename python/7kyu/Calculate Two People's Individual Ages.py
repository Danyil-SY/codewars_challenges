# https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/python

# Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age first) if those exist or null/None or {-1, -1} in C if:

# sum < 0
# difference < 0
# Either of the calculated ages come out to be negative

def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0 or sum_ - difference < 0:
        return None
    return ((difference + round(sum_ - difference) / 2 ), round(sum_ - difference) / 2)
