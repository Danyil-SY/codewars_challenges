# see description here:
# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

# Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

# solve(["abode","ABc","xyzD"]) = [4, 3, 1]
# See test cases for more examples.

# Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

# Good luck!

def solve(strings : list[str]) -> list[int]:
    results = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for s in strings:
        s = s.lower()
        count = 0
        
        for i, char in enumerate(s):
            if i < len(alphabet) and char == alphabet[i]:
                count += 1
        
        results.append(count)
    
    return results