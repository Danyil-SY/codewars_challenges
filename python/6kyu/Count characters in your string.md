# Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

---

```py
from collections import Counter

def count(s):
    return Counter(s)
```

OR

```py
def count(s):
    return {x: s.count(x) for x in s}
```
