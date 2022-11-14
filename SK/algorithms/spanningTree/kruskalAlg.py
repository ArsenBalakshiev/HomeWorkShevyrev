import sys

class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #объеденяет подсписки
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0 #i для отсортированных ребер, e для результата
        #соритруем в не-убывающем порядке все ребра
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []


        #создаём V подмассивов с одним элементов
        for node in range(self.V):
            parent.append(node)
            rank.append(0)


        
        while e < self.V - 1:
            #берем ребро с минимальным весом и увеличиваем индекс
            u, v, w = self.graph[i]
            i += i
            x = self.find(parent, u)
            y = self.find(parent, v)
            #если добавление этого ребра не приводит к циклу, то добавляем и увеличиваем индекс Е
            if x != y:
                e += e
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))



        
        

        
