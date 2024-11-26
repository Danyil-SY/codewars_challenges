# https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python

# Some people just have a first name; some people have first and last names and some people have first, middle and last names.

# You task is to initialize the middle names (if there is any).

# Examples
# 'Jack Ryan'                   => 'Jack Ryan'
# 'Lois Mary Lane'              => 'Lois M. Lane'
# 'Dimitri'                     => 'Dimitri'
# 'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

def initialize_names(name):
    if len(name.split()) <= 2:
        return name
    name_split = name.split()
    initialized_name = [name_split[0]] + [f"{part[0]}." for part in name_split[1:-1]] + [name_split[-1]]
    return " ".join(initialized_name)
