# https://www.codewars.com/kata/54592a5052756d5c5d0009c3/train/python

# Haskell has some useful functions for dealing with lists:

# $ ghci
# GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
# λ head [1,2,3,4,5]
# 1
# λ tail [1,2,3,4,5]
# [2,3,4,5]
# λ init [1,2,3,4,5]
# [1,2,3,4]
# λ last [1,2,3,4,5]
# 5
# Your job is to implement these functions in your given language. Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:

# | HEAD | <----------- TAIL ------------> |
# [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
# | <----------- INIT ------------> | LAST |

# head [x] = x
# tail [x] = []
# init [x] = []
# last [x] = x
# Here's how I expect the functions to be called in your language:

# head([1,2,3,4,5]) => 1
# tail([1,2,3,4,5]) => [2,3,4,5]
# Most tests consist of 100 randomly generated arrays, each with four tests, one for each operation. There are 400 tests overall. No empty arrays will be given. Haskell has QuickCheck tests

def head(argument):
    return argument[0]

def tail(argument):
    return argument[1:]

def init(argument):
    return argument[:-1]

def last(argument):
    return argument[-1]
