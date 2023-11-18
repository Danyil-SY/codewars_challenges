# Pillars

---

There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:

1. number of pillars (≥ 1);
2. distance between pillars (10 - 30 meters);
3. width of the pillar (10 - 50 centimeters).

Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).

---

### Solution

```py
def pillars(num_pill, dist, width):
    return (num_pill-2)*width + (100*dist)*(num_pill-1) if num_pill > 1 else 0
```
