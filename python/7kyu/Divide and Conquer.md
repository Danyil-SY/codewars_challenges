# Divide and Conquer

Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.

---

```py
def div_con(str):
    return sum([x for x in str if isinstance(x, int)]) - sum([int(x) for x in str if not isinstance(x, int)])
```
