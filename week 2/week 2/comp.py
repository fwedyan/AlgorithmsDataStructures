# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:58:43 2024

@author: fwedyan
"""

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Filtering with list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# Create a dictionary where the key is a number and the value is its square
squares_dict = {x: x**2 for x in range(5)}
print(squares)
