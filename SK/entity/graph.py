class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.verts = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def getNodesWithEdges(self, node):
        result = []
        row = self.edges[node]
        for i in range(len(row)):
            if row[i] != -1: result.append(i)

        return result;

    def getNodeWeights(self, node):
        result = []
        row = self.edges[node]
        for i in range(len(row)):
            if row[i] != -1: result.append(row[i])

        return result;

    

    def getFromNodesList(self, edges):
        result = []
        for i in edges:
            result.append(i.fromNode)
        return result

    def copy(self):
        graph = Graph(self.v)
        graph.edges = self.edges
        return graph

    def deleteEdgesForNode(self, node):
        for i in range(len(self.edges[node])):
            self.edges[node][i] = -1

