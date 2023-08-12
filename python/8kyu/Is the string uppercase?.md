# Is the string uppercase?

### Task
Create a method to see whether the string is ALL CAPS.

### Examples (input -> output)
```
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
```
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

---

```py
def sum_mul(n, m):
    if n==0:
        return 'INVALID'
    my_list = [number for number in range(n, m) if number % n == 0]
    sum_list = sum(my_list)
    if sum_list >= 1:
        return sum_list
    elif n < 0 and m <= 0:
        return 'INVALID'
    elif n == m:
        return n - m
    elif n > m:
        return 'INVALID'
```
