# Name Shuffler

Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

```
"john McClane" --> "McClane john"
```

---

```py
def name_shuffler(str):
    return ' '.join( reversed(str.split()) )
```
