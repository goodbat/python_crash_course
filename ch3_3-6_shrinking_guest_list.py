# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written:
# Program purpose:

# Import Section

# Functions

# Variables

# Code
list = ["einstein", "plato", "bill gates", "an alien"]
list.insert(0, "mindy")
list.insert(2, "batman")
list.append("the hulk")
print("Oops, we can only invite 2 people.")
print(len(list))
name = list.pop()
print(name)
name = list.pop()
print(name)
name = list.pop()
print(name)
name = list.pop()
print(name)
name = list.pop()
print(name)
print(list)
print(list[0], "and", list[1], "you are invited.")
del list[0]
del list[0]
print(list)

