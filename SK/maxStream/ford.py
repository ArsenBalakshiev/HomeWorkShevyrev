from pickle import TRUE
from entity.edge import Edge
from collections import deque


class FordGraph:
    def __init__(self):
        self.edges = {}
        self.adjacents = {}

    def add_edge(self, source, sink, capacity):
        if source == sink:
            raise ValueError("Source can not be the Sink.")
        edge = Edge(source, sink, capacity)
        #redge = Edge(source, sink, capacity)
        self.edges[edge] = 0
        #self.edges[redge] = 0

        if source not in self.adjacents:
            self.adjacents[source] = []
        if sink not in self.adjacents:
            self.adjacents[sink] = []

        self.adjacents[source].append(edge)
        #self.adjacents[sink].append(redge)

    def valid_path(self, source, sink, path):
        """ Returns the list of the edges from source to sink """

        if source == sink:
            return path
        for edge in self.adjacents[source]:
            if edge not in path:
                if edge.weight - self.edges[edge] > 0:
                    return self.valid_path(edge.toNode, sink, path + [edge])

        return None

    def max_flow(self, source, sink):

        path = self.valid_path(source, sink, [])

        while (path):
            max_flow = min([edge.weight for edge in path])
            for edge in path:
                self.edges[edge] += max_flow
            path = self.valid_path(source, sink, [])

        return  sum([self.edges[edge] for edge in self.adjacents[source]])

    def printEdges(self):
        for i in self.edges:
            print(i.repr())
