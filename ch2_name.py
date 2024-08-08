# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 7.16.24
# Program purpose: To demonstrate the flexibility of strings

# Import Section

# Functions

# Variables
name = "ada lovelace"

# Code
# Change lowercase string to title csase using the title method.
# Format variable.method()
print(name.title())

# Now change the name to all uppercase and all lowercase
print(name.upper())
print(name.lower())

# Using variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}!"
print(full_name)

#Using variables and methods within a string
print(f"Hello, {full_name.title()}!")

# Make the message a variable then print the message
message = f"Hello, {full_name.title()}!"
print(message)

# Use whitespace to format your output
print("Python")

# Add a tab in front of a string
print("\tPython")

# Break up a string with newline characters
print("Languages:\nPython\nC\nJavaScript")

# Combine the two strategies
print("Languages:\n\tPython\n\tC\n\tJavaScript")