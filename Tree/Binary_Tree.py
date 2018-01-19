class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    # Insert Method
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

    # Traverse : In-order recursive
    def traversInOrder(self):
        if self.root:
            return self.traverseInOrder_Recursive(self.root)

    def traverseInOrder_Recursive(self, node):
        if node.leftChild:
            self.traverseInOrder_Recursive(node.leftChild)

        print(node.value)

        if node.rightChild:
            self.traverseInOrder_Recursive(node.rightChild)

    # Traverse : Pre-order recursive
    def traversePreOrder(self):
        if self.root:
            return self.traversePrerOrder_Recursive(self.root)

    def traversePrerOrder_Recursive(self, node):
        print(node.value)

        if node.leftChild:
            self.traverseInOrder_Recursive(node.leftChild)

        if node.rightChild:
            self.traverseInOrder_Recursive(node.rightChild)

    # Traverse : Post-order recursive
    def traversePostOrder(self):
        if self.root:
            return self.traversePostOrder_Recursive(self.root)

    def traversePostOrder_Recursive(self, node):
        if node.leftChild:
            self.traversePostOrder_Recursive(node.leftChild)

        if node.rightChild:
            self.traversePostOrder_Recursive(node.rightChild)

        print(node.value)

    # Find Minimum Value
    def findMin(self):
        current = self.root
        while(current.leftChild != None):
            current = current.leftChild
        return current.value

    # Find Maximum value
    def findMax(self):
        current = self.root
        while(current.rightChild != None):
            current = current.rightChild
        return current.value





# Test
values = [9, 4, 17, 3, 6, 22, 5, 7, 20, 10]

bst = BinarySearchTree()

for v in values:
    bst.insert(v)

bst.insert(7)
bst.insert(21)

# Traverse : InOrder Recursive
print("TravereInOrder: ")
in_order = bst.traversInOrder()
print(in_order)
print("Traverse PreOrder: ")
pre_order = bst.traversePreOrder()
print(pre_order)
print("Traverse PostOrder: ")
post_order = bst.traversePostOrder()
print(post_order)
print("Find Minimum value in Tree: ")
bst_min = bst.findMin()
print(bst_min)
print("Find maximum value in Tree")
bst_max = bst.findMax()
print(bst_max)
