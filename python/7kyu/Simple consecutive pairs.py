# https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/python

# In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:

# pairs([1,2,5,8,-4,-3,7,6,5]) = 3
# The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
# --the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
# --the second pair is (5,8) and are not consecutive
# --the third pair is (-4,-3), consecutive. Count = 2
# --the fourth pair is (7,6), also consecutive. Count = 3. 
# --the last digit has no pair, so we ignore.

def pairs(arr):
    counter = 0
    for i in range(0, len(arr)-1,2):
        if i+1 > len(arr):
            break
        elif abs(arr[i] - arr[i+1]) == 1:
            counter += 1
    return counter
