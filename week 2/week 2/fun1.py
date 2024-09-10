# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:01:40 2024

@author: fwedyan
"""

# This program demonstrates an argument being
# passed to a function.

def main():
    value = 5
    show_double(value)
    print(value)
    
# The show_double function accepts an argument
# and displays double its value.
def show_double(number):
    number = number * 2
    print(number)

# Call the main function.
main()
