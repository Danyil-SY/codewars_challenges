# Regexp Basics - is it a digit?

---

Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.

---

### Solution

```py
import re
def is_digit(n):
    match = re.findall('[\d]', n)
    return match[0] == n if match else False
```
