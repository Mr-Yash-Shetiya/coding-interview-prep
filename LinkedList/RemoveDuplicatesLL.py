class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,*value):
        self.head = None
        self.tail = None
        self.length = 0
        for value in value:
            self.append(value)

    def append(self,value):
        new = node(value)
        if self.length == 0:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.length += 1
        return new

    def display(self):
        temp = self.head
        ll = []
        while temp:
            ll.append(temp.value)
            temp = temp.next
        print(ll)

    def remove_duplicates_sorted(self):
        temp = self.head

        while temp and temp.next:
            if temp.next.value == temp.value:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self.head

    def remove_duplicates_unsorted(self):
        grab = set()
        current = self.head
        previous = None

        while current:
            if current.value in grab:
                previous.next = current.next
            else:
                grab.add(current.value)
                previous = current
            current = current.next


if __name__ == '__main__':
    l1 = LinkedList(1,2,3,3,3,4)
    l1.append(4)
    l1.append(5)
    l1.display()
    l1.remove_duplicates_sorted()
    l1.display()

    l2 = LinkedList(1,9,3,9,3,4)
    l2.remove_duplicates_unsorted()
    l2.display()


