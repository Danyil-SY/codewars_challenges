# https://www.codewars.com/kata/53cf459503f9bbb774000003/train/python

# Python is now supported on Codewars!

# For those of us who are not very familiar with Python, let's handle the very basic challenge of creating a class named Python. We want to give our Pythons a name, so it should take a name argument that we can retrieve later.

# For example:

# bubba = Python('Bubba')
# bubba.name # should return 'Bubba'

class Python:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
