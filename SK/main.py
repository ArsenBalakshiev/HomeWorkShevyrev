import helpers
from algorithms import depthFirstSearch, breadthFirstSearch, dijkstrasAlgorithm
from algorithms.spanningTree.primAlg import prim
from algorithms.spanningTree.kruskalAlg import KruskalGraph
from maxStream.ford import FordGraph
from maxStream.dinic import DinicGraph

if __name__ == "__main__":
    t = DinicGraph(6)

    helpers.readDKS("data/stream2.json", t)

    print(t.DinicMaxflow(0, 5))