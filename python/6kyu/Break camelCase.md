# Break camelCase

Complete the solution so that the function will break up camel casing, using a space between words.

```
Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

---

```py
def solution(s):
    result = ""
    for letter in s:
        if letter.isupper():
            result += " "
        result += letter
    return result
```
