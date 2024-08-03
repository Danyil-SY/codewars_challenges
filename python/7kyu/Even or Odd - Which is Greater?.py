# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

# Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

# If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

# If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

# If the total of both even and odd numbers are identical return: "Even and Odd are the same"

def even_or_odd(s):
    even_sum = sum(int(num) for num in s if int(num) % 2 == 0)
    odd_sum = sum(int(num) for num in s if int(num) % 2 != 0)
    
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
