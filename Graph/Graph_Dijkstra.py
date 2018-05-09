import sys
import heapq

class Edge(object):
    def __init__(self, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node(object):
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
