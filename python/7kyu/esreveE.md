# esreveR

Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

---

```py
def reverse(lst):
    result = list()
    for item in lst:
        result = [item] + result
    return result
```
