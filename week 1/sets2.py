#Adding elements to sets
seta = {1,2,3,4}
print(seta)
#seta[0] = 5 #does not work, no indexing becuase there is no order
seta.add(5)
print(seta)
seta.add(5)
print(seta)

#add a group of elements
setb = {3,4,5,6}
seta.update(setb) #same as union, but result is in seta
print(seta)

#add an element
#seta.update(7) 
seta.update([7])

#add a list
seta.update([1,7,8])
print(seta)
