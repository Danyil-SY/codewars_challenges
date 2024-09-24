# https://www.codewars.com/kata/58640340b3a675d9a70000b9/train/python

# This Kata is intended as a small challenge for my students

# Create a function that takes a string argument and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").

# Example (Input --> Output)

# "drake" --> "drk"
# "aeiou" --> ""
# remove_vowels("drake") // => "drk"
# remove_vowels("aeiou") // => ""

def remove_vowels(s):
    return ''.join(word for word in s if word not in "aeiou")
