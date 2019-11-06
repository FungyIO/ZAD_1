import directory_filenames
import prepare_data_to_graph
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":

	filenames = directory_filenames.get_current_directory_filenames()
	G = prepare_data_to_graph.prepare_data_to_graph(filenames)

	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G, pos, node_size=1000)
	nx.draw_networkx_edges(G, pos, width=3, arrowsize=30)
	nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')

	plt.show()
