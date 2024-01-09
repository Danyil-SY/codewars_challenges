# Sum of Odd Cubed Numbers

---

Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.

---

### Solution

```py
def cube_odd(arr):
    total = 0 
    for num in arr:
        if (type(num) != int):
            return None
        if num % 2 != 0:
            total += num**3
    return total
```
