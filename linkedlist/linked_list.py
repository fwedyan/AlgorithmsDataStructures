class LinkedList:
    # PART ZERO
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0

    # SECTION 1 FOR STACK LIST ADT
    # PART ONE INSERTION
    def insert_first(self, e):
        newest = self.Node(e, None)
        if self.is_empty(): # in case if the list is empty which is going to happen when it is the first element
            self._head = newest
            self._tail = newest
        else: # in case if the list is not empty
            newest._next = self._head
            self._head = newest
        self._size += 1

    # PART TWO DELETION
    def remove_head(self):
        if self.is_empty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    # PART THREE INSERT TAIL
    def insert_tail(self, e): # same as STACK PUSH
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    # PART FOUR REMOVE TAIL
    def remove_tail(self): # same as STACK POP
        if self.is_empty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        return e

    def middle(self):
        ''' get the middle of the list'''
        if self.is_empty():
            print('List is empty')
            return
        p = self._head
        i = 1
        
        while i< self.__len__()/2:
            p = p._next
            i+=1
        return p._element
    
        
    # SECTION 2 QUEUE LIST ADT
    # PART FIVE INSERT TAIL we already have
    # PART SIX REMOVE HEAD we already have
