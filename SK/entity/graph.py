from collections import deque
import sys

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def getNodesWithEdges(self, node):
        result = []
        row = self.edges[node]
        for i in range(len(row)):
            if row[i] != -1: result.append(i)

        return result;

    def getNodes(self):
        return list(range(0, self.v))
    

    def getNodeWeights(self, node):
        result = []
        row = self.edges[node]
        for i in range(len(row)):
            if row[i] != -1: result.append(row[i])

        return result;

    def getValue(self, node1, node2):
        return self.edges[node1][node2]

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

    def bfs(self, start, end):
        f = False
        visited = []
        node = start
        print("Node - " + str(node))
        stack = deque()
        visited.append(node)
        while len(visited) < self.graph.v:
            for i in self.graph.getNodesWithEdges(node):
                if i not in visited and i not in stack: stack.append(i)
            self.graph.deleteEdgesForNode(node)
            node = stack.popleft() #возвращает элемент с начала контейнера
            if node == end: f = True
            print("Node - " + str(node))
            visited.append(node)
        
        print(visited)
        return f

    def dfs(self, start, end):
        f = False
        visited = []
        node = start
        print("Node - " + str(node))
        stack = deque()
        visited.append(node)
        while len(visited) < self.graph.v:
            for i in self.graph.getNodesWithEdges(node):
                if i not in visited and i not in stack: stack.append(i)
            self.graph.deleteEdgesForNode(node)
            node = stack.pop() #возвращает элемент с начала контейнера
            if node == end: f = True
            print("Node - " + str(node))
            visited.append(node)
        
        print(visited)
        return f

    def fordFulkerson(self, source, sink):

        #для хранения пути, будет заполняться алгоритмом поиска в ширину
        parent = [-1] * self.v
        max_flow = 0

        while(self.bfs(source, sink)):
            path_flow = sys.maxsize
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.edges[parent[s], [s]])
                s = parent[s]
            
            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.edges[u][v] -= path_flow
                self.edges[v][u] -= path_flow
                v = parent[v]
            
        return max_flow


