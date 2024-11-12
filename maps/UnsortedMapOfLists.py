####################################################################
# A map with arrays as values. An element in the array can be reached 
# using a key and index
####################################################################

from maps.unsorted_table_map import UnsortedTableMap


class UnsortedMapOfLists(UnsortedTableMap):

    def __getitem__(self, position: tuple):
        # Write a comment here to explain why we need this if statement
        if len(position) == 1:
            return super().__getitem__(position)

        key, index = position

        head: list = super().__getitem__(key)

        if index >= len(head):
            raise IndexError("Size of array associated with key: ", key, " is: ", len(head))
        return head[index]

    def __setitem__(self, position: tuple, value):

        if len(position) == 1:
            super().__setitem__(position, value)
            return

        key, index = position
        try:

            head: list = super().__getitem__(key)
            if index < len(head):
                # overrite exiting value, or append
                head[index] = value
            elif index == len(head):
                head.append(value)
            else:
                raise IndexError("Size of array associated with key: ", key, " is: ", len(head))

        except KeyError:
            # new key, create a list for the key
            head = [value]
            self._table.append(self._Item(key, head))

    def __delitem__(self, position: tuple):
        """Remove item associated with key k and index, if index not given,
        remove the item (array)
        associated with the key
          raise KeyError if not found
          raise IndexError if index out of bound
          """
        raise Exception("Implement me")

if __name__ == '__main__':
    m = UnsortedMapOfLists()
    m["a", 0] = 5
    m['a', 0] = 50
    m['a', 1] = 60
    m['b', 0] = 2
    m['c', 1] = 10
    m['d'] = [10, 20, 30]
    print(m['a', 0])
    print(m['a', 1])
    print(m['b', 0])
    print(m['a'])
    print(m['d'])

### Test with the following after you implement the required methods
#del m['b', 0]
#del m['c']
