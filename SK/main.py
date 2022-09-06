from helpers import readFile
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    G = readFile("data/graph.json")

    edges = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, seed=7)

    nx.draw_networkx_nodes(G, pos, node_size=700)

    nx.draw_networkx_edges(G, pos, edgelist=edges, width=6, alpha=0.5, edge_color="b", style="dashed")
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plt.show()