# Alternate capitalization

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

---

```py
def capitalize(string):
    even_indexes = ''
    odd_indexes = ''
    for i in range(0, len(string)):
        if i % 2 == 0:
            even_indexes += string[i].upper()
            odd_indexes += string[i]
        else:
            even_indexes += string[i]
            odd_indexes += string[i].upper()
    return [even_indexes, odd_indexes]
```
