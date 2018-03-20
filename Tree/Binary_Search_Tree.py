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

    # Method 1 : print value
    def traversInOrder(self):
        if self.root:
            return self.traverseInOrder_Recursive(self.root)

    def traverseInOrder_Recursive(self, node):
        if node.leftChild:
            self.traverseInOrder_Recursive(node.leftChild)
        print(node.value)
        if node.rightChild:
            self.traverseInOrder_Recursive(node.rightChild)

    # Method 2 : return a list of values
    def traversInOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traverseInOrder_Recursive(node):
                if node.leftChild:
                    traverseInOrder_Recursive(node.leftChild)
                result.append(node.value)
                if node.rightChild:
                    traverseInOrder_Recursive(node.rightChild)
            traverseInOrder_Recursive(self.root)
        return result

    # Traverse : Pre-order recursive

    # Method 1 : print value
    def traversePreOrder(self):
        if self.root:
            return self.traversePrerOrder_Recursive(self.root)

    def traversePrerOrder_Recursive(self, node):
        print(node.value)
        if node.leftChild:
            self.traversePrerOrder_Recursive(node.leftChild)
        if node.rightChild:
            self.traversePrerOrder_Recursive(node.rightChild)

    # Method 2 : return a list of values
    def traversePreOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traversePrerOrder_Recursive(node):
                result.append(node.value)
                if node.leftChild:
                    traversePrerOrder_Recursive(node.leftChild)
                if node.rightChild:
                    traversePrerOrder_Recursive(node.rightChild)
            traversePrerOrder_Recursive(self.root)
        return result

    # Traverse : Post-order recursive

    # Method 1 : print value
    def traversePostOrder(self):
        if self.root:
            return self.traversePostOrder_Recursive(self.root)

    def traversePostOrder_Recursive(self, node):
        if node.leftChild:
            self.traversePostOrder_Recursive(node.leftChild)
        if node.rightChild:
            self.traversePostOrder_Recursive(node.rightChild)
        print(node.value)

    # Method 2 : return a list of values
    def traversePostOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traversePostOrder_Recursive(node):
                if node.leftChild:
                    traversePostOrder_Recursive(node.leftChild)
                if node.rightChild:
                    traversePostOrder_Recursive(node.rightChild)
                result.append(node.value)
            traversePostOrder_Recursive(self.root)
        return result


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

    # Find value
    def find(self, value):
        current = self.root
        while current.value != value:
            if value < current.value:
                current = current.leftChild
            elif value > current.value:
                current = current.rightChild
            if current == None:
                return None
        return current.value

    # Print all the paths from ROOT to LEAF in a Tree. Traverse Inorder.
    def print_all_paths(self):
        path = []
        def print_paths(node, path):
            if node == None:
                return
            path.append(node.value)
            print_paths(node.leftChild, path)
            if node.leftChild == None and node.rightChild == None:
                print(path)
            print_paths(node.rightChild, path)
            path.pop()
        return print_paths(self.root, path)

    # Print values by Level Order
    def level_order(self):
        q = []
        current = self.root
        q.append(current)
        while len(q) > 0:
            current = q[0]
            print(current.value)
            if current.leftChild != None:
                q.append(current.leftChild)
            if current.rightChild != None:
                q.append(current.rightChild)
            q.pop(0)

    # Size of a Binary Tree : Number of nodes in the Tree
    def size_binary_tree(self):
        def size(node):
            if node == None:
                return 0
            return size(node.leftChild) + size(node.rightChild) + 1
        return size(self.root)
