class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new = node(value)
        self.head = new
        self.tail = new
        self.length = 1

    def append(self,value):
        new = node(value)

        if self.head == None:
            self.head = new
            self.tail = new
            self.length += 1
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.length += 1
        return True