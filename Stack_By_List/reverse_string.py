"""
Problem Statement:
Implement a program to reverse a given string using a Stack data structure.

Requirements:
Use a stack to store characters of the string.

Example:
Input:  "hello"
Output: "olleh"
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LL_Stack :
    def __init__(self,value=None):
        self.top = None
        self.height = 0
        if value is not None:
            new = node(value)
            self.top = new
            self.height = 1

    def push(self,value):
        new = node(value)

        if self.top is None:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.height += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value

    def print(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next

def reverse_string(string):
    linked_list_stack = LL_Stack()
    for ch in string:
        linked_list_stack.push(ch)
    reverse = ""
    while linked_list_stack.height > 0:
        reverse += linked_list_stack.pop()

    print("Reversed String :", reverse)
    return reverse

if __name__ == "__main__":
    userinput = str(input("Enter a String: "))
    process = reverse_string(userinput)
    if userinput.lower() == process.lower() :
        print("Palindrome")
