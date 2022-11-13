import sys

def prim(graph, start):
    v = graph.v
    selected_nodes = []
    selected_nodes.append(start)
    result = []
    while len(selected_nodes) < v:
        min = sys.maxsize
        minElementX = 0
        minElementY = 0

        for i in range(len(selected_nodes)):
            neighbours = graph.getNodesWithEdges(selected_nodes[i])
            for j in range(len(neighbours)):
                if graph.getValue(selected_nodes[i], neighbours[j]) < min and neighbours[j] not in selected_nodes:
                    min = graph.getValue(selected_nodes[i], neighbours[j])
                    minElementX = selected_nodes[i]
                    minElementY = neighbours[j]
        
        result.append([minElementX, minElementY])
        selected_nodes.append(minElementY)

    return result