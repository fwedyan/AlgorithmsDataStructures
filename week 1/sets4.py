# removing elements from a list
#Difference between discard() and remove()

# initialize my_set
a = {1, 3, 4, 5, 6}
# discard an element
a.discard(4)
print(a)

# remove an element
a.remove(6)
print(a)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
a.discard(2)
print(a)

# remove an element
# not present in my_set, you will get an exception of type: KeyError

#a.remove(2)

#remove using pop, you will never know which item is removed
print(a.pop())

#remove all elements in the set
a.clear()
print(a)
