import json
from unicodedata import name
import networkx as nx
import matplotlib.pyplot as plt

def readAdjJson(filename):
    graph = {}

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data["data"]:
            graph[i["node"]] = i["edges"]

    return graph;

def readDKS(filename, graph):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data["data"]:
            for j in i["edges"]:
                graph.add_edge(i["node"], j["to"], j["weight"])


def visualizationGraph(dict):
    G = nx.convert.from_dict_of_lists(dict)


    edges = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, seed=7)

    nx.draw_networkx_nodes(G, pos, node_size=700)

    nx.draw_networkx_edges(G, pos, edgelist=edges, width=6, alpha=0.5, edge_color="b", style="dashed")
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    
    plt.show()

def showWeightedGraph(G):
    edges = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, seed=7)

    nx.draw_networkx_nodes(G, pos, node_size=700)

    nx.draw_networkx_edges(G, pos, edgelist=edges, width=6, alpha=0.5, edge_color="b", style="dashed")
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.show()

def containsEdgeWithSameSecondVert(self, list, node):
    F = False
    for i in list:
        if i.toNode == node.name:
            return i
    return None
