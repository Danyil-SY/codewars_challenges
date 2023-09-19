# Factorial

Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

---

```py
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1
```
