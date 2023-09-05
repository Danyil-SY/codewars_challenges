# Most digits

Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

---

```py
def find_longest(arr):
    maximum = ""
    for num in arr:
        num = str(num)
        if len(num) > len(maximum):
            maximum = num
    return int(maximum)
```
