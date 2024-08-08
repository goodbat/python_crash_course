# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written:
# Program purpose:

# Import Section

# Functions

# Variables

# Code
vehicles = ['jeep', 'scooter', 'motorcycle', 'roller blades']
print(vehicles)
vehicles[0] = "big jeep"
print(vehicles)
vehicles.append("mercedes")
print(vehicles)
vehicles.insert(0, "bmw")
print(vehicles)
del vehicles[0]
print(vehicles)
popped_vehicle = vehicles.pop()
print(vehicles)
print(popped_vehicle)
vehicles.remove("motorcycle")
print(vehicles)
vehicles.append("mercedes")
print(vehicles)
too_expensive = "mercedes"
vehicles.remove(too_expensive)
print(vehicles)
print(f"\nA {too_expensive.title()} is too expensive for me.")