# Build Tower Advanced

Build Tower by the following given arguments:

* number of floors (integer and always greater than 0)
* block size (width, height) (integer pair and always greater than (0, 0))
Tower block unit is represented as *. Tower blocks of block size (2, 1) and (2, 3) would look like respectively:

```
  **
  **
  **
  **
```
for example, a tower of 3 floors with block size = (2, 3) looks like below

```
[
  '    **    ',
  '    **    ',
  '    **    ',
  '  ******  ',
  '  ******  ',
  '  ******  ',
  '**********',
  '**********',
  '**********'
]
```
and a tower of 6 floors with block size = (2, 1) looks like below

```
[
  '          **          ', 
  '        ******        ', 
  '      **********      ', 
  '    **************    ', 
  '  ******************  ', 
  '**********************'
]
```
Don't return a whole string containing line-endings but a list/array/vector of strings instead!

This kata might looks like a 5.5kyu one. So challenge yourself!

Go take a look at Build Tower which is a more basic version :)

---

```py
def tower_builder(n, block_size):
    tower = []
    floor_len = n * 2 * block_size[0] - block_size[0]
    
    for i in range(1, n + 1):
        star = '*' * block_size[0] * (i * 2 - 1)
        for j in range(1, block_size[1] + 1):
            tower.append(star.center(floor_len))
    
    return tower
```
