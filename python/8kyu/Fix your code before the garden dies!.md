# Fix your code before the garden dies!

You have an award-winning garden and every day the plants need exactly 40mm of water. You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. Your jealous neighbour hacked your computer and filled your code with bugs.

Your task is to debug the code before your plants die!

---

```py
def rain_amount(rain_amount):
    if (rain_amount < 40):
        return f"You need to give your plant {40 - rain_amount}mm of water"
    else:
        return "Your plant has had more than enough water for today!"
```
