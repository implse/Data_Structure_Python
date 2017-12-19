class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None

class Queue(object):
    def __init__(self):
        self.head = head
        self.tail = tail
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.size > 0:
            self.tail.next_node = new_node
            new_node.next_node = seld.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def dequeue(self, value):
        if self.head == None:
            return None
        result = self.head
        self.head = self.head.previous_node
        self.size -= 1
        return result.data

    def get_size(self):
        return self.size
