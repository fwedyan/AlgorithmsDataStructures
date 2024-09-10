# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:12:33 2024

@author: fwedyan
"""

a = 5      # 0b0101
b = 3      # 0b0011

result = a & b  # 0b0001 (1 in decimal)
print(result)  # Output: 1

result = a | b  # 0b0111 (7 in decimal)
print(result)  # Output: 7

result = a ^ b  # 0b0110 (6 in decimal)
print(result)  # Output: 6

result = ~a  # 0b1010 (-6 in decimal, due to two's complement representation)
print(result)  # Output: -6

result = a << 1  # 0b1010 (10 in decimal)
print(result)  # Output: 10

result = a >> 1  # 0b0010 (2 in decimal)
print(result)  # Output: 2

