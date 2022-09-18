import json
from unicodedata import name
import networkx as nx
import matplotlib.pyplot as plt

def readAdjJsonKruskal(filename, graph):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data["data"]:
            for j in i["edges"]:
                graph.add_edge(i["node"], j["to"], j["weight"])

def readJson(filename, graph):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for i in data["data"]:
            for j in i["edges"]:
                graph.add_edge(i["node"], j["to"], j["weight"])
