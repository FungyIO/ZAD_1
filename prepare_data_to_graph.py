import networkx as nx
import parse_function
import os

 
def prepare_data_to_graph(filenames):
    G = nx.DiGraph()
 
    for node in filenames:
        edges = parse_function.parse_function(node, filenames)

        for edge in edges:
            nodesize = os.path.getsize(node)
            G.add_edge(edge, node + "\n" + str(nodesize))
    return G
