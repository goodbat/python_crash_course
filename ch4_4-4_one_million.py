# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# The exercise asked for a list of numbers up to, and including, 1 million.
# I decided to go to 100 so I wouldn't have to wait for the program to
# complete.

numbers = list(range(1, 101))
for number in numbers:
    print(number)