class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self, limit=1000):
        self.top = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        new_node = Node(value)
        if self.top != None:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size > 0:
            pop_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return pop_value
        else:
            print("Stack is empty")

    def peek(self):
        if self.size > 0:
            return self.top.value
        else:
            print("Stack is empty")        
