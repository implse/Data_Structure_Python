class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = list()
        self.visited = False
        self.predecessor = None

class DepthFirstSearch(object):

    def DFS(self, node):
        node.visited = True
        print("%s" % node.name)

        for n in node.adjacencyList:
            if not n.visited:
                self.DFS(n)

node_1 = Node('A')
node_2 = Node('B')
node_3 = Node('C')
node_4 = Node('D')
node_5 = Node('E')

node_1.adjacencyList.append(node_2)
node_1.adjacencyList.append(node_3)
node_2.adjacencyList.append(node_4)
node_4.adjacencyList.append(node_5)

b = DepthFirstSearch()
b.DFS(node_1)
