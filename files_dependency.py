import directory_filenames
import prepare_data_to_graph
import os
import sys
os.environ["PATH"] += os.pathsep + 'C:/Users/Lenovo/AppData/Local/graphviz-2.38/release/bin'


def files_dependency(path='.'):
	filenames = directory_filenames.get_current_directory_filenames(path)

	G = prepare_data_to_graph.prepare_data_to_graph(filenames, path)
	G.view()


if __name__ == "__main__":
	files_dependency(sys.argv[1])
