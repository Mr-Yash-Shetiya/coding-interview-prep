"""
Problem Statement:
Implement a Stack data structure in Python using a list as the underlying container.

Requirements:
1. The stack should support basic operations:
   - push(value): Insert an element on top of the stack.
   - pop(): Remove and return the top element of the stack. Return None if the stack is empty.
   - size(): Return the number of elements currently in the stack.
   - display(): Print all elements in the stack from bottom to top."""

class List_Stack:
    def __init__(self):
        self.value = None
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def size(self):
        return len(self.stack_list)

    def pop(self):
        if self.size() < 0:
            return None
        else:
            return self.stack_list.pop()

    def display(self):
        if self.size() > 0:
            for item in self.stack_list:
                print(item)

my_stack = List_Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.display()
my_stack.pop()
my_stack.display()