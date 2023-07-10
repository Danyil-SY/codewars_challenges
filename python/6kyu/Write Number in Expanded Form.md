# Write Number in Expanded Form

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

```
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

---

```py
def expanded_form(num):
    result = []
    i = len(str(num)) - 1
    for n in str(num):
        if n != '0':
            result.append(n + '0' * i)
        i -= 1
    return ' + '.join(result)
```
