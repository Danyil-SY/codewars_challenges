# Remove duplicates from list

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

---

```py
def distinct(seq):
    result = []
    for x in seq:
        if x not in result:
            result.append(x)
    return result
```
