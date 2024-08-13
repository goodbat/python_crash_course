# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# Create a list then loop through the list printing a message followed by
# an item from the list.

pizzas = ["peperoni", "cheese", "margarita", "three meat"]
for pizza in pizzas:
    print(f"I like {pizza.title()}")
print("I really like pizza")