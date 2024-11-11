# https://www.codewars.com/kata/567501aec64b81e252000003/train/python

# John wants to decorate the walls of a room with wallpaper. He wants a fool-proof method for getting it right.

# John knows that the rectangular room has a length of l meters, a width of w meters, a height of h meters. The standard width of the rolls he wants to buy is 52 centimeters. The length of a roll is 10 meters. He bears in mind however, that it’s best to have an extra length of wallpaper handy in case of mistakes or miscalculations so he wants to buy a length 15% greater than the one he needs.

# Last time he did these calculations he got a headache, so could you help John?

# Task
# Your function wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must buy.

# Example:
# wallpaper(4.0, 3.5, 3.0) should return "ten"

# wallpaper(0.0, 3.5, 3.0) should return "zero"

# Notes:
# all rolls (even with incomplete width) are put edge to edge

# 0 <= l, w, h (floating numbers); it can happens that w * h * l is zero

# the integer r (number of rolls) will always be less or equal to 20

# FORTH: the number of rolls will be a positive or null integer (not a plain English word; this number can be greater than 20)

# In Coffeescript, Javascript, Python, Ruby and Scala the English numbers are preloaded and can be accessed as:

# numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
# For other languages it is not preloaded and you can instead copy the above list if you desire.

def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", 
               "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
               "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    
    if l == 0 or w == 0 or h == 0:
        return numbers[0]
    
    roll_width = 0.52
    roll_length = 10
    wall_area = 2 * h * (l + w)
    
    rolls_needed = wall_area / (roll_width * roll_length)
    rolls_needed *= 1.15
    rolls_needed = int(-(-rolls_needed // 1))  # Equivalent to math.ceil
    
    return numbers[rolls_needed]
