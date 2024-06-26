# https://www.codewars.com/kata/55c0ac142326fdf18d0000af/train/python

# Hey Codewarrior!

# You already implemented a Cube class, but now we need your help again! I'm talking about constructors. We don't have one. Let's code two: One taking an integer and one handling no given arguments!

# Also we got a problem with negative values. Correct the code so negative values will be switched to positive ones!

# The constructor taking no arguments should assign 0 to Cube's Side property.

class Cube(object):
    def __init__(self, side=0):
        """Constructor that assigns a side value."""
        self.__side = abs(side)
    
    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)
