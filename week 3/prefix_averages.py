# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import random

def prefix_average1(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    total = 0                     # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)          # record the average
  return A

def prefix_average2(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    A[j] = sum(S[0:j+1]) / (j+1)  # record the average
  return A

def prefix_average3(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                   # create new list of n zeros
  total = 0                     # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j]               # update prefix sum to include S[j]
    A[j] = total / (j+1)        # compute average based on current sum
  return A

def createList(lower,upper,size):
    list = []
    for i in range(0,size):
        n= random.randint(lower,upper)
        list.append(n)
    return list

if __name__ == '__main__':
    list1=createList(1,6,10)
    list2 = prefix_average1(list1)
    print(list1)
    for num in list2:
        print("{:.2f}".format(num), end = ' ')  
    