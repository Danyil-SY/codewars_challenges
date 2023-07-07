### String ends with?

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

```
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```

---

```py
def solution(text, ending):
    return text[len(text)-len(ending)::] == ending
```

OR

```py
def solution(text, ending):
    return text.endswith(ending)
```
