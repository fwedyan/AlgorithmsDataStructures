# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:01:09 2024

@author: fwedyan
"""

''' using update method'''

'updating from another dict'
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)
print("this what will happen if we update with an empty dict")
dict3 = {}
dict1.update(dict3)
print(dict1)

''' update using key-value pairs'''
dict1 = {'a': 1, 'b': 2}

dict1.update(b=3, c=4)
print(dict1)

'''update from a list of tuples'''
dict1 = {'a': 1, 'b': 2}

l = list()
l.append(('b', 3))
l.append(('c', 4))
dict1.update(l)
print(dict1)
