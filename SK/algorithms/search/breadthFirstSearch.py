from collections import deque

def bfs(graph, start, end):
    f = False
    visited = []
    node = start
    print("Node - " + str(node))
    stack = deque()
    visited.append(node)
    while len(visited) < graph.v:
        for i in graph.getNodesWithEdges(node):
            if i not in visited and i not in stack: stack.append(i)
        graph.deleteEdgesForNode(node)
        node = stack.popleft() #возвращает элемент с начала контейнера
        if node == end: f = True
        print("Node - " + str(node))
        visited.append(node)
    
    print(visited)
    return f