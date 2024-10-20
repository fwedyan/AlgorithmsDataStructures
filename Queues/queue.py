# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:16:56 2024

@author: fwedyan
"""
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

class Queue:
    
    def __init__(self, type = 'a'):
        self._aqueue:ArrayQueue = None
        self._lqueue:LinkedQueue = None
        self._type = type
        if type == 'a':
            self._aqueue = ArrayQueue()
        else:
            self._lqueue = LinkedQueue()
            
    def __len__(self):
        if self._type =='a':
            return self._aqueue.__len__()
        else:
            return self._lqueue.__len__()
   
    def is_empty(self):
        if self._type =='a':
            return self._aqueue.is_empty()
        else:
            return self._lqueue.is_empty()
      
    def first(self):
      """Return (but do not remove) the element at the front of the queue.
      Raise Empty exception if the queue is empty.
      """
      if self._type =='a':
          return self._aqueue.first()
      else:
          return self._lqueue.first()
      

    def dequeue(self):
     """Remove and return the first element of the queue (i.e., FIFO).

      Raise Empty exception if the queue is empty.
      """
     if self._type =='a':
         return self._aqueue.dequeue()
     else:
         return self._lqueue.dequeue()
  
    def enqueue(self, e):
     if self._type =='a':
         self._aqueue.enqueue(e)
     else:
         self._lqueue.enqueue(e)

if __name__ == '__main__':      
     q  = Queue('l')
     q.enqueue(1)
     q.enqueue(2)
     q.enqueue(3)
     q.enqueue(4)
     q.enqueue(10)   
     while not q.is_empty():
         print(q.dequeue(), end = ' ')
        