# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Chapter 4, exercise 4-11

# This program creates a list and creates a copy of the list. Next, items
# are added to the original list and the copied list, followed by print
# statements to show that both lists changed and are now not equal in content.

my_pizzas = ["peperoni", "cheese", "margarita", "three meat"]
friends_pizzas = my_pizzas[:]
print(my_pizzas)
print(friends_pizzas)
my_pizzas.append("sausage")
friends_pizzas.append("anchovy")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)