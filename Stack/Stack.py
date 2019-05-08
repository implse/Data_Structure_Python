class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.top != None:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        pop_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pop_value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value
