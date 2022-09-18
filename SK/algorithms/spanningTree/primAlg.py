
def prim(graph):
    postitive_inf = float('inf')
    v = graph.v
    edges = graph.edges
    selected_nodes = [False for node in range(v)]
    result = [[0 for column in range(v)] 
                for row in range(v)]
    index = 0

    while(False in selected_nodes):

        minimum = postitive_inf

        start = 0
        end = 0

        for i in range(v):
            if selected_nodes[i]:
                for j in range(v):
                    if (not selected_nodes[j] and edges[i][j] != -1):  
                        if edges[i][j] < minimum:
                            minimum = edges[i][j]
                            start, end = i, j
        
        selected_nodes[end] = True

        result[start][end] = minimum

        if minimum == postitive_inf:
            result[start][end] = 0

        print("(%d.) %d - %d: %d" % (index, start, end, result[start][end]))
        index += 1
        
        result[end][start] = result[start][end]

        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))