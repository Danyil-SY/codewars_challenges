# https://www.codewars.com/kata/56576f82ab83ee8268000059/train/python

# Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
# For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']

def spacey(array):
    output = []
    combined = ''
    for word in array:
        combined += word
        output.append(combined)
    return output
