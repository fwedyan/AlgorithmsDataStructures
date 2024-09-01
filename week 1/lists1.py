a = [] #this is an empty list
a = [1,2,3]
#how to access list elements?
print(a[0])
print(a[1])
print(a[2])
#list elements are indexed 0.. length-1
#but
print(a[-1]) #last element, as you are saying length-1
print(a[-2]) # length -2
print(a[-3]) # length-3
#print(a[-4])  out f index, error
# print(a[3]) out of index, error
# You can have different types in the list
a = [1,2,'my name', 2.5]
#you can also have an element as a list
b = [1,a,3]
#you do not need to remember how many elements you have in a list
s =len(a)
print('size of list',s)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a)
print(b)
