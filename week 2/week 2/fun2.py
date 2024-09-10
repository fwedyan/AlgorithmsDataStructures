# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:13:06 2024

@author: fwedyan
"""

def simple_generator():
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3

# Create a generator object
gen = simple_generator()
# Iterate through the generator
print(next(gen))  # Output: "First yield" followed by 1
print(next(gen))  # Output: "Second yield" followed by 2
print(next(gen))  # Output: "Third yield" followed by 3

# If you call next(gen) again, it will raise StopIteration since the generator is exhausted
