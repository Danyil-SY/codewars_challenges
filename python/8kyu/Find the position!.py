# https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python

# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    letter = alphabet.lower()
    position = ord(letter) - ord('a') + 1
    return f"Position of alphabet: {position}"
