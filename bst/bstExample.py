from bst.binary_search_tree import TreeMap
import random

bst = TreeMap()
for i in range(0,10000):
    r = random.randint(1,6)
    bst[r] = 1 + bst.get(r, 0) #defined in class Mapping 
    

for (num, freq) in bst.items():
    print(num,freq)

for i,j in bst.find_range(1,4):
    print(i,j)

print(bst[1])
print(bst.get(1))


