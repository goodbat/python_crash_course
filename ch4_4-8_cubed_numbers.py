# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# This program raises numbers to the 3rd power (cubes the numbers).

cubed_numbers = []
for value in range(1, 11):
    cube = value ** 3
    cubed_numbers.append(cube)
for number in cubed_numbers:
    print(number)