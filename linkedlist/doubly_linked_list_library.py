import doubly_linked_list as dll

def printDlist(dlist):
    tmp_dlist = dll.DoublyLinkedList()
    while not dlist.is_empty():
        element = dlist.delete_head()
        if not dlist.is_empty():
            print(element, end='->')
        else:
            print(element)
        tmp_dlist.insert_tail(element)
    #print("tmp_dlist._head._next._element:", tmp_dlist._head._next._element, "tmp_dlist._head._next._next._next._element", tmp_dlist._head._next._next._next._element, "prev of 5", tmp_dlist._head._next._next._next._prev._element )
    while not tmp_dlist.is_empty(): 
        element = tmp_dlist.delete_head()
        dlist.insert_tail(element) 



if __name__ == "__main__":
    my_dlist = dll.DoublyLinkedList()

    my_dlist.insert_head(1) # [1]
    my_dlist.insert_head(3) # [3, 1]
    my_dlist.insert_head(5) # [5, 3, 1]
    my_dlist.insert_head(7) # [7, 5, 3, 1]
    my_dlist.insert_head(9) # [9, 7, 5, 3, 1]
    printDlist(my_dlist)
    print(my_dlist)
    
    print("del head:",my_dlist.delete_head())
    print(my_dlist)
    print("del tail:",my_dlist.delete_tail())

    print(my_dlist)
   #  print()
    my_dlist.insert_head(9)
    my_dlist.insert_tail(1)
    print(my_dlist)
    
    print()
    ptr = my_dlist._head._next
    print("moving:", ptr._element)
    ptr = ptr._next
    print("moving:", ptr._element)
    ptr = ptr._next
    print("moving:", ptr._element)
    my_dlist.insert_after(ptr,99)
    printDlist(my_dlist)
   #  my_dlist.delete_current(ptr) 
   #  printDlist(my_dlist)
    ptr = my_dlist._head._next
    #my_dlist.delete_current(ptr) 
   #  #print()
    printDlist(my_dlist)
    ptr = my_dlist._tail._prev
   #  my_dlist.delete_current(ptr) 
   # #printDlist(my_dlist)
   #  print(my_dlist)

