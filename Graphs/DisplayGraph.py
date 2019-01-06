import networkx as nx
import pylab

"""
Displays graph with nodes' and edges' labels.
Arguments: G - reference to networkx graph
Return: nothing

"""
def displayGraph(G):
    pos = nx.spring_layout(G)
    # get edges' labels
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    nx.draw(G, pos, node_size = 300, with_labels = True)
    pylab.savefig("graph.png")
    pylab.show()

