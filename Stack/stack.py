class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class stack:
    def __init__(self,value):
        new = node(value)
        self.top = new
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

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
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

user_action_stack = stack(1)
user_action_stack.push(2)
user_action_stack.push(3)
print("After Push : ")
user_action_stack.print_stack()
user_action_stack.pop()
print("After Pop : ")
user_action_stack.print_stack()



