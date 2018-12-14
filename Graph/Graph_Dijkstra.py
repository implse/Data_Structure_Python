# GRAPH : DIJKSTRA'S ALGORITHM

import sys
import heapq

class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = list()
        self.minDistance = sys.maxsize

    def __cmp__(self, otherNode):
        return self.cmp(self.minDistance, otherNode.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

class Edge(object):
    def __init__(self, weight, startNode, targetNode):
        self.weight = weight
        self.startNode = startNode
        self.targetNode = targetNode

class Dijkstra(object):
    def calculateShortestPath(self, nodeList, startNode):
        q = list()
        heapq.heapify(q)
        startNode.minDistance = 0
        heapq.heappush(q, startNode)

        while len(q) > 0:
            actualNode = heapq.heappop(q)
            for edge in actualNode.adjacencyList:
                u = edge.startNode
                v = edge.targetNode
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q, v)

    def getShortestPath(self, startNode, targetNode):
        print("Shortest distance between %s and %s is : %d" %(startNode.name, targetNode.name, targetNode.minDistance))

        Path_from_start_to_end = list()
        Node = targetNode
        while Node is not None:
            Path_from_start_to_end.append(Node.name)
            Node = Node.predecessor
        print("The path is: " + " ".join(Path_from_start_to_end[::-1]))

# Test1 Directed Graph
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")

edge1 = Edge(5, node_A, node_B)
edge2 = Edge(8, node_A, node_H)
edge3 = Edge(9, node_A, node_E)
edge4 = Edge(15, node_B, node_D)
edge5 = Edge(12, node_B, node_C)
edge6 = Edge(4, node_B, node_H)
edge7 = Edge(7, node_H, node_C)
edge8 = Edge(6, node_H, node_F)
edge9 = Edge(5, node_E, node_H)
edge10 = Edge(20, node_E, node_G)
edge11 = Edge(1, node_F, node_C)
edge12 = Edge(13, node_F, node_G)
edge13 = Edge(3, node_C, node_D)
edge14 = Edge(11, node_C, node_G)
edge15 = Edge(9, node_D, node_G)

node_A.adjacencyList.append(edge1)
node_A.adjacencyList.append(edge2)
node_A.adjacencyList.append(edge3)
node_B.adjacencyList.append(edge4)
node_B.adjacencyList.append(edge5)
node_B.adjacencyList.append(edge6)
node_H.adjacencyList.append(edge7)
node_H.adjacencyList.append(edge8)
node_E.adjacencyList.append(edge9)
node_E.adjacencyList.append(edge10)
node_F.adjacencyList.append(edge11)
node_F.adjacencyList.append(edge12)
node_C.adjacencyList.append(edge13)
node_C.adjacencyList.append(edge14)
node_D.adjacencyList.append(edge15)

nodeList = (node_A, node_B, node_C, node_D, node_E, node_F, node_G, node_H)
dj = Dijkstra()
dj.calculateShortestPath(nodeList, node_A)
dj.getShortestPath(node_A, node_G)

# Test 2 Undirected Graph
node_A = Node("S") # Start
node_B = Node("A")
node_C = Node("B")
node_D = Node("C")
node_E = Node("D")
node_F = Node("E") # End
node_G = Node("F")
node_H = Node("G")
node9 = Node("H")
node_A0 = Node("I")
node_A1 = Node("J")
node_A2 = Node("K")
node_A3 = Node("L")

# S neighbors
edge1 = Edge(7, node_A, node_B) # A
edge2 = Edge(2, node_A, node_C) # B
edge3 = Edge(3, node_A, node_D) # C
# A neighbors
edge4 = Edge(7, node_B, node_A) # S
edge5 = Edge(3, node_B, node_C) # B
edge6 = Edge(4, node_B, node_E) # D
# B neighbors
edge7 = Edge(2, node_C, node_A) # S
edge8 = Edge(3, node_C, node_B) # A
edge9 = Edge(4, node_C, node_E) # D
edge10 = Edge(1, node_C, node9) # H
# D neighbors
edge11 = Edge(4, node_E, node_B) # A
edge12 = Edge(4, node_E, node_C) # B
edge13 = Edge(5, node_E, node_G) # F
# F neighbors
edge14 = Edge(5, node_G, node_E) # D
edge15 = Edge(3, node_G, node9) # H
# H neighbors
edge16 = Edge(1, node9, node_C) # B
edge17 = Edge(3, node9, node_G) # F
edge18 = Edge(2, node9, node_H) # G
# G neighbors
edge19 = Edge(2, node_H, node9) # H
edge20 = Edge(2, node_H, node_F) # E
# E neighbors
edge21 = Edge(5, node_F, node_A2) # K
edge22 = Edge(5, node_F, node_H) # G
# K neighbors
edge23 = Edge(5, node_A2, node_F) # E
edge24 = Edge(4, node_A2, node_A0) # I
edge25 = Edge(4, node_A2, node_A1) # J
# I neighbors
edge26 = Edge(4, node_A0, node_A2) # K
edge27 = Edge(6, node_A0, node_A1) # J
edge28 = Edge(4, node_A0, node_A3) # L
# J neighbors
edge29 = Edge(4, node_A1, node_A2) # K
edge30 = Edge(6, node_A1, node_A0) # I
edge31 = Edge(4, node_A1, node_A3) # I
# L neighbors
edge32 = Edge(4, node_A3, node_A0) # I
edge33 = Edge(4, node_A3, node_A1) # J
edge34 = Edge(2, node_A3, node_D) # C
# C neighbors
edge35 = Edge(2, node_D, node_A3) # L
edge36 = Edge(3, node_A3, node_A) # S

# Node S
node_A.adjacencyList.append(edge1)
node_A.adjacencyList.append(edge2)
node_A.adjacencyList.append(edge3)
# Node A
node_B.adjacencyList.append(edge4)
node_B.adjacencyList.append(edge5)
node_B.adjacencyList.append(edge6)
# Node B
node_C.adjacencyList.append(edge7)
node_C.adjacencyList.append(edge8)
node_C.adjacencyList.append(edge9)
node_C.adjacencyList.append(edge10)
# Node C
node_D.adjacencyList.append(edge35)
node_D.adjacencyList.append(edge36)
# Node D
node_E.adjacencyList.append(edge11)
node_E.adjacencyList.append(edge12)
node_E.adjacencyList.append(edge13)
# Node E
node_F.adjacencyList.append(edge21)
node_F.adjacencyList.append(edge22)
# Node F
node_G.adjacencyList.append(edge17)
node_G.adjacencyList.append(edge15)
# Node G
node_H.adjacencyList.append(edge19)
node_H.adjacencyList.append(edge20)
# Node H
node9.adjacencyList.append(edge16)
node9.adjacencyList.append(edge17)
node9.adjacencyList.append(edge18)
# Node I
node_A0.adjacencyList.append(edge26)
node_A0.adjacencyList.append(edge27)
node_A0.adjacencyList.append(edge28)
# Node J
node_A1.adjacencyList.append(edge29)
node_A1.adjacencyList.append(edge30)
node_A1.adjacencyList.append(edge31)
# Node K
node_A2.adjacencyList.append(edge23)
node_A2.adjacencyList.append(edge24)
node_A2.adjacencyList.append(edge25)
# Node L
node_A3.adjacencyList.append(edge32)
node_A3.adjacencyList.append(edge33)
node_A3.adjacencyList.append(edge34)

nodeList = (node_A, node_B, node_C, node_D, node_E, node_F, node_G, node_H, node9, node_A0, node_A1, node_A2, node_A3)
dj = Dijkstra()
dj.calculateShortestPath(nodeList, node_A)
dj.getShortestPath(node_A, node_F)
