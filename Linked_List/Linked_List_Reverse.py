class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseList(r):
    current_node = r
    next_node = None
    previous_node = None
    while current_node != None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node
