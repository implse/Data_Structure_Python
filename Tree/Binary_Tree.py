class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = None(value)

    def insertNode(self, value, node):
        if value < node.value:
            if node.leftChild:
                self.insertNode(value, node.leftChild)
            else:
                node.leftChild = Node(value)
        else:
            if node.rightChild:
                self.insertNode(value, node.rightChild)
            else:
                node.rightChild = Node(value)
