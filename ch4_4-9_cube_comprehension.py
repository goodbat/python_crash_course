# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# This program uses a one-line method for assigning values to items in a
# list. In essence, the first line of code can be done with a for loop as
# shown below.
# for value in range(1, 11):
#     cube = value ** 3
#     cubed_numbers.append(cube)

cubed_numbers = [value**3 for value in range(1, 11)] 
for number in cubed_numbers:
    print(number)