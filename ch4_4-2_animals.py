# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# Create a list of animals then loop through the list, and print formatted
# output to display the animals' name embedded in a message.

animals = ["dog", "cat", "moose", "horse"]
for animal in animals:
    print(f"A {animal.title()} would make a good pet.")
print("All of these animals have four legs.")