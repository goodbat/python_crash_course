# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Demonstration how a for loop works

# Create a list of odd numbers from 1 to 21. This is done by starting
# with 1 and incrementing the number by 2 (stepping by 2). The number 1
# is an odd number because it cannot be evently divided by 2.

odd_numbers = list(range(1, 21, 2))

print(odd_numbers)

for number in odd_numbers:
    print(number)