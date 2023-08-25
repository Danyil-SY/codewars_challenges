# No oddities here

Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.

---

```py
def no_odds(values):
    return [x for x in values if x % 2 == 0]
```
