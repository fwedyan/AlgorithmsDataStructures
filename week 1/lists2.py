import random
'''write a function to  create and return a list
the list size and range of random numbers are passed
 as parameters to the list'''

def createList(a,b,n):
    list = []
    for i in range(0,n):
        n= random.randint(a,b)
        list.append(n)
    return list
def main():
    list1=createList(1,6,5)
    list2=createList(1,6,5)
    print(list1)
    print(list2)
    # print(list1[0:1])
    # print(list1[:-len(list1)+1])
    #list[0:5]=[1,1,1,1,1]
    list3 = list1+list2
    list4 = list1*2
    list4+=list4
    print("list 3: ", list3)
    print("list 4: ", list4)
    
    for x in list1:
        print(x)
    if not 555 in list4:
        print("no")
    else:
        print("yes")
    
    
    
main()
        
