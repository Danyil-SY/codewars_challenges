# https://www.codewars.com/kata/55960bbb182094bc4800007b/train/python

# Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-') between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3.

# Note that the number will always be non-negative (>= 0).

def insert_dash(num):
    dashed = ""
    num_str = str(num)
    for i in range(len(num_str)):
        if i > 0 and int(num_str[i-1]) % 2 != 0 and int(num_str[i]) % 2 != 0:
            dashed += "-"
        dashed += num_str[i]
    return dashed
