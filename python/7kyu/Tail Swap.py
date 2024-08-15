# https://www.codewars.com/kata/5868812b15f0057e05000001/train/python

# You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

# Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.

# Examples
# ["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
# ["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]

def tail_swap(strings):
    split_1 = strings[0].split(':')
    split_2 = strings[1].split(':')
    return [split_1[0]+':'+split_2[1],split_2[0]+':'+split_1[1]] 
