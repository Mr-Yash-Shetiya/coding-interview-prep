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

user_action_stack = stack(1)
user_action_stack.print_stack()



