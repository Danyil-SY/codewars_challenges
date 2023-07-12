# Rock Paper Scissors!

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

```
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
```

---

```py
def rps(p1, p2):
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rules[p1] == p2:
        return 'Player 1 won!'
    if rules[p2] == p1:
        return 'Player 2 won!'
    return 'Draw!'
```
