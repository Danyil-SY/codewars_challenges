# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python

# Given a string of space separated words, return the longest word.
# If there are multiple longest words, return the rightmost longest word.

# Examples
# "red white blue"  =>  "white"
# "red blue gold"   =>  "gold"

def longest_word(string_of_words):
    return max(string_of_words.split(), key=lambda word: (len(word), string_of_words.rfind(word)))
