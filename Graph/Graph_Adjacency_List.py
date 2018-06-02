class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbors(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph(object):
    vertices = dict()

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbors(v)
                if key == v:
                    value.add_neighbors(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

# Test 1
g = Graph()
a = Vertex('A')
g.add_vertex(a)
b = Vertex('B')
g.add_vertex(b)

for i in range(ord('A'), ord('K')):
    v = Vertex(chr(i))
    g.add_vertex(v)

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
