# Python Crash Course, Third Edition, by Eric Matthes
# Code written by: Michael Batty
# Date written: 7.19.24
# Exercise: 2-7, page 25
# Program purpose: Create a name variable with whitespace characters at the
# beginning and end, then use use the three stripping methods to remove
# whitespace.

famous_philosopher = "\tRene Descartes\t\n"

__name__ == 'main'
print(famous_philosopher)
print(f"lstrip, {famous_philosopher.lstrip()}")
print(f"rstrip, {famous_philosopher.rstrip()}")
print(f"strip, {famous_philosopher.strip()}")