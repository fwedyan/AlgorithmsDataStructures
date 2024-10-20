# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:23:28 2024

@author: fwedyan
"""
from array_queue import ArrayQueue
from Stacks.array_stack import ArrayStack
from QueueExamples import printQueue

''' Print the queue in reverse order, from tail to head'''
def printReverse(q:ArrayQueue):
   tempStack =ArrayStack ()
   tempQueue = ArrayQueue()
   while not q.is_empty():
       tempStack.push(q.first())
       tempQueue.enqueue(q.dequeue())
   while not tempQueue.is_empty():
       q.enqueue(tempQueue.dequeue())
       print(tempStack.pop(), end = ' ')
       
   print()

''' Write a function that merges two given queues element 
by element. The created queue is then returned by the
 function. Both given two queues will be empty after
 calling the function
 ex: q1 = [1,2,3,4,10], q2 = [5,6,7]
 result = [1,5,2,6,3,7,4,10]
 
 '''
def merge(q1:ArrayQueue, q2:ArrayQueue ):
    result = ArrayQueue()
    while not q1.is_empty() and not q2.is_empty():
        result.enqueue(q1.dequeue())
        result.enqueue(q2.dequeue())
    while not q1.is_empty():
        result.enqueue(q1.dequeue())
    while not q2.is_empty():
         result.enqueue(q2.dequeue())
    return result     
         
'''Write a function to find the highest integer value in
 a queue. the function throws an exception when the queue
 has no intgeres at all.'''
def findMaxInt(q:ArrayQueue):
     pass
 
'''Write a function to split a given queue into two queues
element by element. The orignal given queue should not
be lost
 ex:  q = [1,2,3,4,5,6,7]
 result [1,3,5,7], [2,4,6]'''
def split(q:ArrayQueue):
     q1 = ArrayQueue()
     q2 = ArrayQueue()
     
if __name__ == '__main__':      
    q  = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(10)
    
    q2 = ArrayQueue()
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    
   # printReverse(q)
   # printReverse(q)
    res = merge(q,q2)
    printQueue(res)

