from bst.binary_search_tree import TreeMap
import random
#what is this code doing?

bst = TreeMap()
for i in range(0,10000):
    r = random.randint(1,6)
    bst[r] = 1 + bst.get(r, 0) #defined in class Mapping 
    #bst[r] = 1+ bst.get(r)
    
#for (num, freq) in bst.items():
   # print(num,freq)
    
for i,j in bst.find_range(1,4):
    print(i,j)

print(bst[1])
print(bst.get(1))
print(bst.find_gt(4))

