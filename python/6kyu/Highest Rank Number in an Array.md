# Highest Rank Number in an Array

---

Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
```
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
```

---

### Solution

```py
def highest_rank(arr):
    sorted_dict = dict(sorted(frequency(arr).items(), key=lambda item: (item[1], item[0])))
    return list(sorted_dict.keys())[-1]

def frequency(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        elif num not in count_dict:
            count_dict[num] = 1
    return count_dict
```
