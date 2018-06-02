import sys
import heapq

class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = list()
        self.minDistance = sys.maxsize

    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

class Dijkstra(object):
    def calculateShortestPath(self, vertexList, startVertex):
        q = list()
        heapq.heapify(q)
        startVertex.minDistance = 0
        heapq.heappush(q, startVertex)

        while len(q) > 0:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.adjacencyList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q, v)

    def getShortestPath(self, targetVertex):
        print("Shortest distance between vertex is :", targetVertex.minDistance)

        Vertex = targetVertex
        while Vertex is not None:
            print("%s " % Vertex.name)
            Vertex = Vertex.predecessor

# Test1 Directed Graph
node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")
node4 = Vertex("D")
node5 = Vertex("E")
node6 = Vertex("F")
node7 = Vertex("G")
node8 = Vertex("H")

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)


node1.adjacencyList.append(edge1)
node1.adjacencyList.append(edge2)
node1.adjacencyList.append(edge3)
node2.adjacencyList.append(edge4)
node2.adjacencyList.append(edge5)
node2.adjacencyList.append(edge6)
node8.adjacencyList.append(edge7)
node8.adjacencyList.append(edge8)
node5.adjacencyList.append(edge9)
node5.adjacencyList.append(edge10)
node5.adjacencyList.append(edge11)
node6.adjacencyList.append(edge12)
node6.adjacencyList.append(edge13)
node3.adjacencyList.append(edge14)
node3.adjacencyList.append(edge15)
node4.adjacencyList.append(edge16)

vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)
dj = Dijkstra()
dj.calculateShortestPath(vertexList, node1)
dj.getShortestPath(node7)

# Test 2 Undirected Graph
node1 = Vertex("S") # Start
node2 = Vertex("A")
node3 = Vertex("B")
node4 = Vertex("C")
node5 = Vertex("D")
node6 = Vertex("E") # End
node7 = Vertex("F")
node8 = Vertex("G")
node9 = Vertex("H")
node10 = Vertex("I")
node11 = Vertex("J")
node12 = Vertex("K")
node13 = Vertex("L")

# S neighbors
edge1 = Edge(7, node1, node2) # A
edge2 = Edge(2, node1, node3) # B
edge3 = Edge(3, node1, node4) # C
# A neighbors
edge4 = Edge(7, node2, node1) # S
edge5 = Edge(3, node2, node3) # B
edge6 = Edge(4, node2, node5) # D
# B neighbors
edge7 = Edge(2, node3, node1) # S
edge8 = Edge(3, node3, node2) # A
edge9 = Edge(4, node3, node5) # D
edge10 = Edge(1, node3, node9) # H
# D neighbors
edge11 = Edge(4, node5, node2) # A
edge12 = Edge(4, node5, node3) # B
edge13 = Edge(5, node5, node7) # F
# F neighbors
edge14 = Edge(5, node7, node5) # D
edge15 = Edge(3, node7, node9) # H
# H neighbors
edge16 = Edge(1, node9, node3) # B
edge17 = Edge(3, node9, node7) # F
edge18 = Edge(2, node9, node8) # G
# G neighbors
edge19 = Edge(2, node8, node9) # H
edge20 = Edge(2, node8, node6) # E
# E neighbors
edge21 = Edge(5, node6, node12) # K
edge22 = Edge(5, node6, node8) # G
# K neighbors
edge23 = Edge(5, node12, node6) # E
edge24 = Edge(4, node12, node10) # I
edge25 = Edge(4, node12, node11) # J
# I neighbors
edge26 = Edge(4, node10, node12) # K
edge27 = Edge(6, node10, node11) # J
edge28 = Edge(4, node10, node13) # L
# J neighbors
edge29 = Edge(4, node11, node12) # K
edge30 = Edge(6, node11, node10) # I
edge31 = Edge(4, node11, node13) # I
# L neighbors
edge32 = Edge(4, node13, node10) # I
edge33 = Edge(4, node13, node11) # J
edge34 = Edge(2, node13, node4) # C
# C neighbors
edge35 = Edge(2, node4, node13) # L
edge36 = Edge(3, node13, node1) # S

# Node S
node1.adjacencyList.append(edge1)
node1.adjacencyList.append(edge2)
node1.adjacencyList.append(edge3)
# Node A
node2.adjacencyList.append(edge4)
node2.adjacencyList.append(edge5)
node2.adjacencyList.append(edge6)
# Node B
node3.adjacencyList.append(edge7)
node3.adjacencyList.append(edge8)
node3.adjacencyList.append(edge9)
node3.adjacencyList.append(edge10)
# Node C
node4.adjacencyList.append(edge35)
node4.adjacencyList.append(edge36)
# Node D
node5.adjacencyList.append(edge11)
node5.adjacencyList.append(edge12)
node5.adjacencyList.append(edge13)
# Node E
node6.adjacencyList.append(edge21)
node6.adjacencyList.append(edge22)
# Node F
node7.adjacencyList.append(edge17)
node7.adjacencyList.append(edge15)
# Node G
node8.adjacencyList.append(edge19)
node8.adjacencyList.append(edge20)
# Node H
node9.adjacencyList.append(edge16)
node9.adjacencyList.append(edge17)
node9.adjacencyList.append(edge18)
# Node I
node10.adjacencyList.append(edge26)
node10.adjacencyList.append(edge27)
node10.adjacencyList.append(edge28)
# Node J
node11.adjacencyList.append(edge29)
node11.adjacencyList.append(edge30)
node11.adjacencyList.append(edge31)
# Node K
node12.adjacencyList.append(edge23)
node12.adjacencyList.append(edge24)
node12.adjacencyList.append(edge25)
# Node L
node13.adjacencyList.append(edge32)
node13.adjacencyList.append(edge33)
node13.adjacencyList.append(edge34)

vertexList = (node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13)
dj = Dijkstra()
dj.calculateShortestPath(vertexList, node1)
dj.getShortestPath(node6)
