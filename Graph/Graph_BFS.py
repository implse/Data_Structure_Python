class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = list()
        self.visited = False
        self.predecessor = None

class BreadthFirstSearch(object):

    def BFS(self, startNode):
        queue = list()
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print("%s" % actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

node_1 = Node('A')
node_2 = Node('B')
node_3 = Node('C')
node_4 = Node('D')
node_5 = Node('E')

node_1.adjacencyList.append(node_2)
node_1.adjacencyList.append(node_3)
node_2.adjacencyList.append(node_4)
node_4.adjacencyList.append(node_5)

b = BreadthFirstSearch()
b.BFS(node_1)
