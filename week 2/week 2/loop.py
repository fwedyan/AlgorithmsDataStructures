# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:47:44 2024

@author: fwedyan
"""

x = 1
while x<10:
    y=1
    while (y<x):
        print("*", end=' ')
        y+=1
    print()
    x+=1