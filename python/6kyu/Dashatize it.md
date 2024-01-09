# Dashatize it

---

Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

```
274 -> '2-7-4'
6815 -> '68-1-5'
```

---

### Solution

```py
def dashatize(num):
    if not num and not (num == 0):
        return 'None'

    result = '-'.join(str(abs(num)))
    copy_result = result[:]
    occurrences = 0

    for index, value in enumerate(result):
        if value == '-':
            if int(result[index - 1]) % 2 == 0 and int(result[index + 1]) % 2 == 0:
                copy_result = copy_result[:index - occurrences] + copy_result[index + 1 - occurrences:]
                occurrences += 1

    return copy_result
```
