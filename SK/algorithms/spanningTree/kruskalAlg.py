def find_subtree(self, parent, i):
    if parent[i] == i:
        return i
    return self.find_subtree(parent, parent[i])

def connect_subtrees(self, parent, subtree_sizes, x, y):
    xroot = self.find_subtree(parent, x)
    yroot = self.find_subtree(parent, y)
    if subtree_sizes[xroot] < subtree_sizes[yroot]:
        parent[xroot] = yroot
    elif subtree_sizes[xroot] > subtree_sizes[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        subtree_sizes[xroot] += 1

def kruskals_mst(graph):
    result = []
    
    i = 0
    e = 0

    v = graph.v
    edges = graph.edges
    edges = sorted(edges, key=lambda item: item[2])
    print(edges)
    
    parent = []
    subtree_sizes = []

    for node in range(v):
        parent.append(node)
        subtree_sizes.append(0)


    while e < (v - 1):
        node1, node2, weight = edges[i]
        i = i + 1

        x = find_subtree(parent, node1)
        y = find_subtree(parent, node2)

        if x != y:
            e = e + 1
            result.append([node1, node2, weight])
            connect_subtrees(parent, subtree_sizes, x, y)
    
    for node1, node2, weight in result:
        print("%d - %d: %d" % (node1, node2, weight))