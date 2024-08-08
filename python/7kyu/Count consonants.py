# https://www.youtube.com/watch?v=NUz4QK1l0fA&list=OLAK5uy_mR7cseUWoq8uksFqr-HLKbnHobVvE43H4

# Complete the function that takes a string of English-language text and returns the number of consonants in the string.

# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

def consonant_count(s):
    return sum(1 for char in s if char.lower() in "bcdfghjklmnpqrstvwxyz")
