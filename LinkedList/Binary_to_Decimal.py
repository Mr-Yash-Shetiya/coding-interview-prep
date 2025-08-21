#Problem statement: Convert Binary to decimal in a linked list

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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def binary_to_decimal(self):
        self.reverse()
        temp = self.head
        var = 0
        pos = 0
        while temp:
            if temp.value != 0:
                var = var + 2**pos
            pos += 1
            temp = temp.next
        self.reverse()
        return var

l1 = LinkedList(1,1,0,1)
print(l1.binary_to_decimal())