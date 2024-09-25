# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:29:34 2024

@author: fwedyan
"""
import sys
import array

list1 = {1,2,3, 'name'}
x = 100
print(sys.getsizeof(x))
myarray = array.array('i', [1,2,3,4,10,15,20,22])
print(sys.getsizeof(myarray))
