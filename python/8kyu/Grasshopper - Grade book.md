# Grasshopper - Grade book

Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
```
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
```
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

---

```py
def get_grade(s1, s2, s3):
    grade = (s1 + s2 + s3) / 3
    if grade >= 90 and grade <= 100: return 'A'
    elif grade >= 80 and grade < 90: return 'B'
    elif grade >= 70 and grade < 80: return 'C'
    elif grade >= 60 and grade < 70: return 'D'
    else: return 'F'
```
