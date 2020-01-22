import networkx as nx
import parse_filenames
from graphviz import Digraph
import os

 
def prepare_data_to_graph(filenames, path='.', max_num_of_nodes=60):
    G = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    G.attr(size='6,6')

    for node in filenames:
        edges = parse_filenames.parse_function(node, filenames, path)

        max_num_of_nodes -= 1
        if max_num_of_nodes < 0:
            break

        for edge in edges:
            node_size = os.path.getsize(node)
            G.edge(edge, node.split('/')[-1] + "\n" + str(node_size))
    return G

