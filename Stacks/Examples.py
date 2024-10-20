from array_stack import ArrayStack

'''create a copy of the stack'''
def copy(source, dest):
   temp = ArrayStack()
   while not source.is_empty():
       temp.push(source.top())
       source.pop()
   while not temp.is_empty():
       dest.push(temp.top())
       source.push(temp.pop())
         
'''print from top to bottom'''
def printStack(s:ArrayStack):
  print("from top: ", end = ' ')
  temp = ArrayStack()
  while not s.is_empty():
      print(s.top(), end = ' ')
      temp.push(s.pop())
  print()   
  while not temp.is_empty():
      s.push(temp.pop())

   # S= [1,
   #    2
   #     ,3,
   #     10
   #     ,5] top =1
def swapFirstTwo(s:ArrayStack):
   if len(s) >=2:
     first = s.pop()
     second = s.pop()
     s.push(first)
     s.push(second)
   #...
   #s = [2,
   #     1,
   #     3,
   #     10
   #     ,5] top = 2 
''' Write a function to swap the top and 
bottom of a given stack'''
def swapTopBottom(s:ArrayStack()):
    temp = ArrayStack()
    if len(s) >=2:
      top =s.top()
    while not s.is_empty():
        temp.push(s.top())
        bottom = s.pop()
    temp.pop()
    temp.push(top)
    while len(temp)>1:
        s.push(temp.pop())
    s.push(bottom)    
    
if __name__ == '__main__':        
 s1 = ArrayStack()
 # x = 1
 # y = 2
 # s1.push(x)
 # s1.push(y)
 # x = s1.pop()
 # y = s1.pop()
 # print(x)
 # print(y)
 
 s2 = ArrayStack()
 s1.push(1)
 s1.push(2)
 s1.push(3)
 s1.push(4)
 s1.push(5)
 printStack(s1)
# swapFirstTwo(s1)
# copy(s1,s2)
# printStack(s2)
 swapTopBottom(s1)
 printStack(s1)
 