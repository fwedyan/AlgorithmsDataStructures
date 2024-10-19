class DoublyLinkedList:
    # PART ZERO
    class Node:
        __slots__ = '_element', '_prev', '_next'            # streamline memory
        def __init__(self, element,next = None,prev = None):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = self.Node(element=None, next=None, prev=None)
        self._tail = self.Node(element=None, next=None, prev=None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    # list of functions: is_empty, insert_after, insert_before, insert_head, insert_tail, delete_head, delete_tail, delete_current
    def is_empty(self):
        return self._size == 0
    
    """Add element e between two existing nodes and return new node."""
    def _insert_between(self, e, predecessor, successor):
   
     newest = self._Node(e, predecessor, successor)      # linked to neighbors
     predecessor._next = newest
     successor._prev = newest
     self._size += 1
     return newest
 
    # PART TWO
    def insert_after(self, elementObject, new_element):
        new_node = self.Node(new_element, elementObject._next, elementObject)
        elementObject._next._prev = new_node
        elementObject._next = new_node
        self._size += 1

    def insert_before(self, element, new_element):
        new_node = self.Node(new_element, element, element._prev)
        element._prev._next = new_node
        element._prev = new_node
        self._size += 1
        
    def insert_head(self, element):
        new_node = self.Node(element, self._head._next, self._head)
        self._head._next._prev = new_node
        self._head._next = new_node
        self._size += 1


    def insert_tail(self, element):
        new_node = self.Node(element, self._tail, self._tail._prev)
        self._tail._prev._next = new_node
        self._tail._prev = new_node
        self._size += 1
    #print("new_node._prev:", new_node._prev._element, "element:", new_node._element, "new_node._next:",new_node._next._element)

    # PART THREE
    def _delete_current(self, node): # fix that element .prev._element is None
        if self.is_empty():
            raise Exception("List is empty")
        if self._head._next == node:
            return self.delete_head()
        if self._tail._prev == node:
            return self.delete_tail()
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        return node._element
    
    def delete_head(self):
        if self.is_empty():
            raise Exception("List is empty")
        element = self._head._next._element
        self._head._next = self._head._next._next
        self._head._next._prev = self._head
        self._size -= 1
        return element
    def delete_tail(self):
        if self.is_empty():
            raise Exception("List is empty")
        element = self._tail._prev._element
        self._tail._prev = self._tail._prev._prev
        self._tail._prev._next = self._tail
        self._size -= 1
        return element

    # PART FOUR
    def __len__(self):
        return self._size
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            s = "["
            #traversing
            current = self._head._next
            while current._next != self._tail:
                s += str(current._element) + ", "
                current = current._next
            s += str(current._element) + "]"
            return s
