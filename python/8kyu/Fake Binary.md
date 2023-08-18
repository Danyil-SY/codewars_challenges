# Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

---

```py
def fake_bin(x):
    return ''.join('0' if int(item) < 5 else '1' for item in x)
```
