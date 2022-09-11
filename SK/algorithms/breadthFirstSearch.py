from collections import deque

def bfs(dgraph, start, end):
    f = False
    graph = dgraph.copy()
    visited = []
    node = start
    print("Node - " + str(node))
    stack = deque()
    visited.append(node)
    while True:
        for i in graph.getNodesWithEdges(node):
            if i not in visited and i not in stack: stack.append(i)
        if len(stack) == 0: break
        print(stack)
        graph.deleteEdgesForNode(node)
        node = stack.popleft()
        if node == end: f = True
        print("Node - " + str(node))
        visited.append(node)
    
    print(visited)
    return f