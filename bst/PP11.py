from bst.binary_search_tree import TreeMap
from bst.avl_tree import AVLTreeMap
import random

def create(size, value = 1):
    bst = AVLTreeMap()     # or you can use TreeMap()
    counter = 0
    while counter<size:
        val = random.randint(1,1000)
        if not val in bst.keys():
            bst[val] = value
            counter +=1
    return bst

bst = create(32)
print(bst.height())
