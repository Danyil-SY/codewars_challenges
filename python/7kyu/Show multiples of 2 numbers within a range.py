# https://www.codewars.com/kata/583989556754d6f4c700018e/train/python

# Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd parameter.

# Python, Javascript, Java, Ruby versions: return results in a list/array

# NOTICE:

# Do NOT worry about checking zeros or negative values.
# To find out if 3rd parameter (the upper limit) is inclusive or not, check the tests, it differs in each translation

def multiples(s1,s2,s3):
    return [i for i in range(1, s3) if i % s1 == 0 and i % s2 == 0]
