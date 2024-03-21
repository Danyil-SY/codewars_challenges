# https://www.codewars.com/kata/559f44187fa851efad000087/train/python

# Write a function that removes every lone 9 that is inbetween 7s.

# "79712312" --> "7712312"
# "79797"    --> "777"

def seven_ate9(str_):
    return str_.replace("797", "77").replace("797", "77")
