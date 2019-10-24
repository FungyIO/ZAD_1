import networkx as nx
import parse_function
 
 
def prepare_data_to_graph(names):
    G = nx.DiGraph()
 
    for node in names:
        edges = parse_function.parse_function(node, names)
        for edge in edges:
            G.add_edge(edge, node)
    return G
