import helpers
import networkx as nx
import matplotlib.pyplot as plt
from algorithms import depthFirstSearch, breadthFirstSearch, dijkstrasAlgorithm
from entity.graph import Graph
from algorithms.spanningTree.primAlg import prim
from algorithms.spanningTree.kruskalAlg import kruskals_mst

if __name__ == "__main__":
    Graph = Graph(6)
    helpers.readDKS("data/dks.json", Graph)
    kruskals_mst(Graph)
    