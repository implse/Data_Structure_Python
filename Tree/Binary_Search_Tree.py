# BINARY SEARCH TREE

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
            # left Sub Tree
            if node.left:
                self.insertNode(value, node.left)
            else:
                node.left = Node(value)
        else:
            # right Sub Tree
            if node.right:
                self.insertNode(value, node.right)
            else:
                node.right = Node(value)

    # Remove Method
    def removeNode(self, value):
        if self.root:
            return self.remove(value, self.root)

    def remove(self, value, node):
        if node == None:
            return node
        # Searching Node.value
        if value < node.value:
            node.left = self.remove(value, node.left)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        else:
            # Case 1: No child
            if node.left == None and node.right == None:
                del node
                return None
            # Case 2: One child
            elif node.left == None:
                tempNode = node.right
                del node
                return tempNode
            elif node.right == None:
                tempNode = node.left
                del node
                return tempNode
            # Case 3: Two Children
            else:
                tempNode = self.getPredecessor(node.left)
                node.value = tempNode.value
                node.left = self.remove(tempNode.value, node.left)
        return node

    # Find predecessor
    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

    # Traverse : In-order recursive

    # Method 1 : print value
    def traversInOrder(self):
        if self.root:
            return self.traverseInOrder_Recursive(self.root)

    def traverseInOrder_Recursive(self, node):
        if node.left:
            self.traverseInOrder_Recursive(node.left)
        print(node.value)
        if node.right:
            self.traverseInOrder_Recursive(node.right)

    # Method 2 : return a list of values
    def traversInOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traverseInOrder_Recursive(node):
                if node.left:
                    traverseInOrder_Recursive(node.left)
                result.append(node.value)
                if node.right:
                    traverseInOrder_Recursive(node.right)
            traverseInOrder_Recursive(self.root)
        return result

    # Traverse : Pre-order recursive

    # Method 1 : print value
    def traversePreOrder(self):
        if self.root:
            return self.traversePrerOrder_Recursive(self.root)

    def traversePrerOrder_Recursive(self, node):
        print(node.value)
        if node.left:
            self.traversePrerOrder_Recursive(node.left)
        if node.right:
            self.traversePrerOrder_Recursive(node.right)

    # Method 2 : return a list of values
    def traversePreOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traversePrerOrder_Recursive(node):
                result.append(node.value)
                if node.left:
                    traversePrerOrder_Recursive(node.left)
                if node.right:
                    traversePrerOrder_Recursive(node.right)
            traversePrerOrder_Recursive(self.root)
        return result

    # Traverse : Post-order recursive

    # Method 1 : print value
    def traversePostOrder(self):
        if self.root:
            return self.traversePostOrder_Recursive(self.root)

    def traversePostOrder_Recursive(self, node):
        if node.left:
            self.traversePostOrder_Recursive(node.left)
        if node.right:
            self.traversePostOrder_Recursive(node.right)
        print(node.value)

    # Method 2 : return a list of values
    def traversePostOrder(self):
        if not self.root:
            return None
        else:
            result = []
            def traversePostOrder_Recursive(node):
                if node.left:
                    traversePostOrder_Recursive(node.left)
                if node.right:
                    traversePostOrder_Recursive(node.right)
                result.append(node.value)
            traversePostOrder_Recursive(self.root)
        return result


    # Find Minimum Value
    def findMin(self):
        current = self.root
        while(current.left != None):
            current = current.left
        return current.value

    # Find Maximum value
    def findMax(self):
        current = self.root
        while(current.right != None):
            current = current.right
        return current.value

    # Find value
    def find(self, value):
        current = self.root
        while current.value != value:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
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
            print_paths(node.left, path)
            if node.left == None and node.right == None:
                print(path)
            print_paths(node.right, path)
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
            if current.left != None:
                q.append(current.left)
            if current.right != None:
                q.append(current.right)
            q.pop(0)

    # Size of a Binary Tree : Number of nodes in the Tree
    def size_binary_tree(self):
        def size(node):
            if node == None:
                return 0
            return size(node.left) + size(node.right) + 1
        return size(self.root)
