import networkx as nx
import parse_function
import os
 
 
def prepare_data_to_graph(filenames):
    G = nx.DiGraph()
 
    for node in filenames:
        edges = parse_function.parse_function(node, filenames)
        node_size = 0

        for edge in edges:
            for root, dirs, files in os.walk("."):
                for filename in files:
                    if filename == node:
                        node_size = os.path.getsize(filename)
            G.add_edge(edge, node + "\n" + str(node_size))
    return G
