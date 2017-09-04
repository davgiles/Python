class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            # always do this â€“ saves a lot
                                  # of headaches later!
    def getData(self):
        return self.data            # returns a POINTER

    def getNext(self):
        return self.next            # returns a POINTER

    def setData(self, newData):
        self.data = newData         # changes a POINTER

    def setNext(self,newNext):
        self.next = newNext         # changes a POINTER

class LinkedList(object):

    def __init__(self):
        self.head = None

    def __str__(self):

        s = ''
        current = self.head
        
        while current != None:
            s += (current.getData() + '  ')
            current = current.getNext()

        return s

    def addFirst(self, item):
        # Add an item to the beginning of the list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def addLast(self, item):
        # Add an item to the end of a list
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def addInOrder(self, item):
        # Insert an item into the proper place of an ordered list.
        # This assumes that the original list is already properly
        #    ordered.
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getLength(self):
        # Return the number of items in the list
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def findUnordered(self, item):
        # Search in an unordered list
        #    Return True if the item is in the list, False
        #    otherwise.
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def findOrdered(self, item):
        # Search in an ordered list
        #    Return True if the item is in the list, False
        #    otherwise.
        # This method MUST take advantage of the fact that the
        #    list is ordered to return quicker if the item is not
        #    in the list.
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def delete(self, item):
        # Delete an item from an unordered list
        #    if found, return True; otherwise, return False
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def copyList(self):
        # Return a new linked list that's a copy of the original,
        #    made up of copies of the original elements
        copy = LinkedList()
        current = self.head

        while current != None:
            copy.addLast(current.getData())
            current = current.getNext()

        return copy

    def reverseList(self):
        # Return a new linked list that contains the elements of the
        #    original list in the reverse order.
        reverse = LinkedList()
        current = self.head

        while current != None:
            reverse.addFirst(current.getData())
            current = current.getNext()

        return reverse

    def orderList(self):
        # Return a new linked list that contains the elements of the
        #    original list arranged in ascending (alphabetical) order.
        #    Do NOT use a sort function:  do this by iteratively
        #    traversing the first list and then inserting copies of
        #    each item into the correct place in the new list.
        ordered = LinkedList()
        current = self.head

        while current != None:
            ordered.addInOrder(current.getData())
            current = current.getNext()

        return ordered

    #def isOrdered(self):

    # Return True if a list is ordered in ascending (alphabetical)
    #    order, or False otherwise

    def isEmpty(self):
        # Return True if a list is empty, or False otherwise
        return self.head == None

    #def mergeList(self, b):

    # Return an ordered list whose elements consist of the
    #    elements of two ordered lists combined.

    #def isEqual(self, b):

    # Test if two lists are equal, item by item, and return True.

    #def removeDuplicates(self):

    # Remove all duplicates from a list, returning a new list.
    #    Do not change the order of the remaining elements.

def main():

    mylist = LinkedList()
    mylist.addFirst('5')
    mylist.addFirst('10')
    mylist.addFirst('15')
    mylist.addFirst('20')
    mylist.addLast('50')
    mylist.addLast('100')

    print(mylist)

    mylist2 = mylist.copyList()
    print(mylist2)
    mylist3 = mylist.reverseList()
    print(mylist3)
    mylist4 = mylist.orderList()
    print(mylist4)

main()
