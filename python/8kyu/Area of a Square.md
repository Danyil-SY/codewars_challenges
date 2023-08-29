# Area of a Square

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

---

```py
import math

def square_area(num):
    return round(((num * 4) / (math.pi * 2)) ** 2, 2)
```
