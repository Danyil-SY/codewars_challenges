# (* https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python

# Move every letter in the provided string forward 10 letters through the alphabet.

# If it goes past 'z', start again at 'a'.

# Input will be a string with length > 0. *)

def move_ten(st):
    shifted_string = ""
    shift = 10
    for char in st:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            shifted_string += new_char
        else:
            shifted_string += char
    return shifted_string
