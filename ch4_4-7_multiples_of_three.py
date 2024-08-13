# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# This program will multiply each number in a range by 3. Note that the
# range is from 1 to 10, however, the range statement uses 11 as the last
# number.

numbers = []
for value in range(1, 11):
    multiple = value * 3
    numbers.append(multiple)
for number in numbers:
    print(number)