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
            self.root = Node(value)
        else:
            self.insertNode(value, self.root)

    def insertNode(self, value, node):
        if value < node.value:
            # Left Sub Tree
            if node.leftChild:
                self.insertNode(value, node.leftChild)
            else:
                node.leftChild = Node(value)
        else:
            # Right Sub Tree
            if node.rightChild:
                self.insertNode(value, node.rightChild)
            else:
                node.rightChild = Node(value)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.value

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.value

    # Traverse : InOrder
    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.value)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
