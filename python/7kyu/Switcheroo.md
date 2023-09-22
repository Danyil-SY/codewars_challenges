# Switcheroo

Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

```
'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
```

---

```py
def switcheroo(s):
    switch = {'a': 'b', 'b': 'a', 'c': 'c'}
    return ''.join(switch[x] for x in s)
```
