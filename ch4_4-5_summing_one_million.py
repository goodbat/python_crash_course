# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# Using a list of numbers from 1 to 1,000,000, print the minimum, maximum,
# and sum of the numbers. Notice the underscore in place of the comma
# delimiter. This is a python feature that makes reading numbers easier
# while avoiding confusion when the interpreter sees a comma in a number.

numbers = list(range(1, 1_000_001))
print(f"The lowest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The summ of the numbers is {sum(numbers)}")