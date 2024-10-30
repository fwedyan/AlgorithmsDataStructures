import random
import enum
from abc import ABC, abstractmethod

from PriorityQueues.heap_priority_queue import HeapPriorityQueue

'Enum class, similiar to enums in Java, C, C++,...'
class SortingALgorithm(enum.Enum):
    PR_Queue = 1
    SortedPriorityQueue = 2
    UnSortedPriorityQueue =3

'Abstract class'
class Sorter(ABC):

    @abstractmethod
    def sort(self) -> list:
        """in strategy pattern naming, this is method execute"""
        pass


class PR_queue_sorter(Sorter):
    """ Heap sort Sorting according to the algorithm on slide #10 using a heap implementation
    of priority queue"""

    def __init__(self):
        self._q = HeapPriorityQueue()

    def sort(self, seq:list):
        while len(seq) > 0:
            self._q.add(seq[0], None)
            del seq[0]
        while not self._q.is_empty():
            k,v =self._q.remove_min()
            seq.append(k)
        return seq


class Context:
    def __init__(self, sorting_algo:SortingALgorithm):
        if sorting_algo == SortingALgorithm.PR_Queue:
            self._sorter = PR_queue_sorter()

    def strategy(self):
        """    The Context maintains a reference to one of the Strategy objects. The
               Context does not know the concrete class of a strategy. It should work
               with all strategies via the Strategy interface.
               In our example: Strategy interface: Sorter
               Strategy objects: PR_Queue,

               """
        return self._strategy

    def strategy(self, sorter: Sorter) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._sorter = sorter

    def sort(self, seq:list):
        return self._sorter.sort(seq)  # delegation

if __name__ == "__main__":

    l1 = [random.randint(0, 100) for i in range(5)]
    print(l1)
    c = Context(SortingALgorithm.PR_Queue)
    l1 = c.sort(l1)
    print(l1)

    #you can use the same strategy more than once
    l2 = [random.randint(0, 100) for i in range(10)]
    print(l2)
    c = Context(SortingALgorithm.PR_Queue)
    l2 = c.sort(l2)

    print(l2)
