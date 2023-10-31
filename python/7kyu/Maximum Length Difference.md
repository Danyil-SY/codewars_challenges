# Maximum Length Difference

---

You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
```
Bash note:
* input : 2 strings with substrings separated by ,
* output: number as a string

---

### Solution

```py
def mxdiflg(a1, a2):
    if len(a1) < 1 or len(a2) < 1:
        return -1
    
    min_a1 = len(min(a1, key=len))
    max_a1 = len(max(a1, key=len))
    min_a2 = len(min(a2, key=len))
    max_a2 = len(max(a2, key=len))
    
    possibility1 = max_a2 - min_a1
    possibility2 = max_a1 - min_a2
    
    return max(possibility1, possibility2)
```
