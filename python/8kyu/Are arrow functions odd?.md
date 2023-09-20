# Are arrow functions odd?

Time to test your basic knowledge in functions! Return the odds from a list:

```
[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
```

---

```py
def odds(nums):
    return [x for x in nums if x % 2 != 0]
```
