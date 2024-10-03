from array_queue import ArrayQueue

''' duplciate each queue entry
example: a,b,c--> a,a, b,b,c,c'''
def duplicateQueueEntries(q:ArrayQueue):
   pass    

''' duplicate the queue 
example: a,b,c --> a,b,c,a,b,c
'''
def duplicateQueue(q:ArrayQueue):
    copy1 = ArrayQueue()
    copy2 = ArrayQueue()
    while not q.is_empty():
       copy1.enqueue(q.first())
       copy2.enqueue(q.first())
       q.dequeue()
    while not copy1.is_empty():
        q.enqueue(copy1.dequeue())
    while not copy2.is_empty():
        q.enqueue(copy2.dequeue())
        

''' printing the queue, starting from head(front)'''
def printQueue(q:ArrayQueue()):
    tempQ = ArrayQueue()
    print("starting from the fron: ", end = ' ')
    while not q.is_empty():
       tempQ.enqueue(q.first())
       print(q.dequeue(), end = ' ') 
    while not tempQ.is_empty():
        q.enqueue(tempQ.dequeue())
        
    print()


q = ArrayQueue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
duplicateQueue(q)
printQueue(q)
duplicateQueue(q)

printQueue(q)
#print(q.is_empty())
