import json
import networkx as nx

def readFile(filename):
    g = nx.Graph()
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data["nodes"]:
            g.add_node(i["name"])
        for j in data["edges"]:
            g.add_edge(j["from"], j["to"], weight = j["weight"])
    return g
