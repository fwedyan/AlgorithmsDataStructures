# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:21:52 2024

@author: fwedyan
"""

#A generator function looks like a normal function
# but contains one or more yield statements. 
#When called, it doesn't execute the function's code
# but returns a generator object. 
#You can then iterate over this object to retrieve 
#values one at a time.
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
gen = countdown(5)

# Iterate through the generator
for number in gen:
    print(number)
