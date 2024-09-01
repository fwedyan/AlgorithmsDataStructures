import random
#write a function to fill create and return a list, the list size is n, which is
# a aparamer, the array is filled with random numbers in a given range
def createList(a,b,n):
    list = []
    for i in range(0,n):
        n= random.randint(a,b)
        list.append(n)
    return list
def copyList(source):
    target= []
    target+=source
    return target
def main():
    list1=createList(1,6,5)
    list2=copyList(list1)
    list2.append("new value")
    print("list1=",list1)
    print("list2=",list2)
    #Shallow copy- be careful!
    list3=list2
    list3.remove("new value")
    print("list2=",list2)
main()
        
