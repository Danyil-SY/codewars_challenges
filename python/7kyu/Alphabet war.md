# Alphabet war

---

### Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

### Task
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

```
 w - 4
 p - 3
 b - 2
 s - 1
```
The right side letters and their power:

```
 m - 4
 q - 3
 d - 2
 z - 1
```
The other letters don't have power and are only victims.

### Example
```
AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!
```

---

### Solution

```py
def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_side_result = 0
    right_side_result = 0
    for char in fight:
        if char in left_side:
            left_side_result += left_side.get(char)
        if char in right_side:
            right_side_result += right_side.get(char)
    return 'Left side wins!' if left_side_result > right_side_result\
    else 'Right side wins!' if right_side_result > left_side_result else "Let's fight again!"
```
