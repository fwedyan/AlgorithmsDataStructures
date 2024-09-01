#creating sets
#1. containing values, use { }, but add items (not pairs)
seta = {1,2,3,4,1,2}
print(seta)
#check type
print(type(seta))
#2. creating an empty set
setb = set()
#Note, using empty { } will not create a list, it will create a dictionary
imNotList = {}
print(type(setb))
print(type(imNotList))

#3. from a list
list1=[1,2,3,4,5,5,4]
setc=set(list1)
print(setc)
