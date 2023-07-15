# Sum of numbers from 0 to N

Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

```
> 6
```
Output:

```
0+1+2+3+4+5+6 = 21
```

Input:

```
> -15
```
Output:

```
-15<0
```

Input:

```
> 0
```
Output:

```
0=0
```

---

```py
def show_sequence(n):
    if n < 0:
        return '{}<0'.format(n)
    elif n == 0:
        return '{}=0'.format(n)
    else:
        sequence = '+'.join(map(str, range(0, n+1)))
        total = sum(range(0, n+1))
        return '{} = {}'.format(sequence, total)
```
