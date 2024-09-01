#adding to a list
a = {1,2,3}
b =  { 4,5}
c = set()
#you can add sets, two or more
c.update(a,b, {11})
print(c)
#add lists and sets
c.update([15,25], {4,41})
print(c)
