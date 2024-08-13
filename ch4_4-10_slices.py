# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 8.8.24
# Program purpose: Exercise 4-10

# This program prints three slices of a list.

car_brands = ["Ford", "BMW", "Audi", "Chevy", "Dodge", "Mercedes"]
car_brands.sort()
print(car_brands)
print("The first three cars are", car_brands[0:3])
print("The middle two cars are", car_brands[2:4])
print("The last three cars are", car_brands[-3:])