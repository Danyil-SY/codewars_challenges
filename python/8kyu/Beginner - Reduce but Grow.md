# Beginner - Reduce but Grow

Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

---

```py
def grow(arr):
    result = 1
    for el in arr:
        result *= el
    return result
```
