import linked_list as ll

'''print the list!'''
def printList(llist:ll.LinkedList):
    # create a new linked list
    new_llist = ll.LinkedList()
    # traverse the linked list and add the elements on the new linked list
    while not llist.is_empty(): 
        element = llist.remove_head()
        if not llist.is_empty():
            print(element, end='->')
        else:
            print(element)
        new_llist.insert_first(element)

    while not new_llist.is_empty(): # un-reverse the list
        element = new_llist.remove_head()
        llist.insert_first(element)
    
'''implement at home!, reverse a given list'''
def reverseList(llist:ll.LinkedList()):
    # use a stack
    pass


if __name__ == "__main__":
    # create a linked list 
    my_list = ll.LinkedList()
    my_list.insert_first(1)
    my_list.insert_first(3)
    my_list.insert_first(5)
    my_list.insert_first(7)
    my_list.insert_first(9)
    my_list.insert_first(11)
    my_list.insert_first(13)
    my_list.insert_first(15)    

    printList(my_list)
    print(my_list.middle())

# =============================================================================
#     # Test deleting
#     print("Deleted Head: ", my_list.remove_head())
#     printList(my_list)
# 
#     # insert on tail
#     print("Insert (append) 11 on Tail")
#     my_list.insert_tail(11)
#     printList(my_list)
# 
#     # delete tail
#     print("Deleted Tail: ", my_list.remove_tail())
#     printList(my_list)
# =============================================================================
