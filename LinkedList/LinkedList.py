"""Linked List with the following functions:"""
from enum import nonmember


#   1. Creation of New_node
#       A. 1. Class New_Node
#          2. New_Node.value = value
#          3. New_Node.next = none
#          Creation of New_node: Pass new node to Class New_Node
#   1. Constructor : __init__
#       B. 1. Pass new node to Class New_Node [new_node = NewNode(value)]
#          2. Set up self.head = new_node
#          3. Set up self.tail = new_node
#          4. Set up self.length = 1
#
#   2. Append
#       1. Creation New Node: [new_node = NewNode(value)]
#       2. tail → node
#
#   3. Pop
#       1. 2 temporary nodes pointing to start
#       2. Move the first node ahead to search empty data
#       3. Keep storing 1st node in 2nd
#       4. When empty found -
#                 #tail is 2nd node,
#                 #current tail ptr will be none
#                 #decrement length
#
#   4. Display
#       1. Iteration From start: temp_node = self.head
#       2. Print value and go to next
#
#   5. Prepend
#       1. New_node → next = self.head
#       2. self.head = New_node
#       3. Increase length
#
#   6. Pop first
#       1. Require Temp_Node
#       2. Temp_Node pointing to the first node's head
#       3. The First Node's head will be the second Node's head
#       4. Temp node's head will be none
#
#   7. Insert Node
#   8. Remove Node
#   9. Reverse
#
#   10.Get by index
#       1. Check index validation
#       2. Require Temp_Node [ temp = self.head ]
#       3. Loop till given index- and return-last node value
#   11.Set at index
#       1. Check index validation
#       2. Require Temp_Node [ temp = self.head ]
#       3. Loop till given index
#       4. Update temp_node value with user argument value
#Constructor
class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    #Create a new node
    def __init__(self, value):
        new_node = NewNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Time Complexity: O(n)"""
        "Step1 : Iteration From start to end"
        "Iteration happens in LL with help of Node"
        "Start means go from self.head"
        temp_node = self.head

        while temp_node :
                print(temp_node.value)
                temp_node = temp_node.next

    def append(self, value):
        """Time Complexity: O(1)"""
        #Append: Add node at last so no head data to be update
        #Step1: Creation of New Node
        new_node = NewNode(value)

        #Step2: Check if LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #Add at last - So only tail will update not head
        else:
            self.tail.next = new_node
            self.tail = new_node
        #Step3: update length
        self.length += 1
        return True

    def pop(self):
        """Time Complexity: O(n)"""
        #Approach
        #Step1: 2 temporary nodes pointing to start
        #Step2: Move first node ahead to search empty data
        #Step3: Keep storing 1st node in 2nd
        #Step4: When empty found -
                #tail is 2nd node,
                #current tail ptr will be a none
                #decrement length
        if self.length == 0:
            return None

        temp_node = self.head
        prev_node = self.head

        while(temp_node.next):
            prev_node = temp_node
            temp_node = temp_node.next

        self.tail = prev_node
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp_node

    def pop_first(self):
        """Time Complexity: O(1)"""
        if self.length == 0:
            return None
        temp_node = self.head
        self.head = self.head.next
        temp_node.head = None
        self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            return temp_node.value

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return None
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.value = value
            return temp_node.value

    def insert_node(self,index,value):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.head = NewNode(value)
        else:
            new_node = NewNode(value)

            prev_node = self.head
            temp_node = self.head
            for _ in range(index):
                prev_node = temp_node
                temp_node = temp_node.next
            prev_node.next = new_node
            new_node.next = temp_node
            self.length += 1
            return True

    def reverse(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node
        after = temp_node.next
        before = None
        for _ in range(self.length):
            after = temp_node.next
            temp_node.next = before
            before = temp_node
            temp_node = after

ll = LinkedList(1)
ll.append(2)
ll.append(5)
ll.append(4)
print("Linked list after append 2 :")
print(ll.print_list())
# ll.pop_first()
# print("\nLinked list after pop 2 :")
# print(ll.print_list())
# print("\n Value at index 1 is :",ll.get(1))
# print("\n Value changed at index 1 is :",ll.set(1,50))
#
# print(ll.print_list())
# ll.insert_node(0,5)
# print("\n LL after inserting :")
# print(ll.print_list())
ll.reverse()
print("\n LL after reversing :")
print(ll.print_list())


