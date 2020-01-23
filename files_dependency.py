import directory_filenames
import prepare_data_to_graph
import os
import sys

from git_repo_latest_commit_hash import get_git_commit_hash

os.environ["PATH"] += os.pathsep + 'C:/Users/Lenovo/AppData/Local/graphviz-2.38/release/bin'


def files_dependency(path='.'):
	filenames = directory_filenames.get_current_directory_filenames(path)

	if len(sys.argv) >= 3:
		max_num_of_nodes = int(sys.argv[2])
	else:
		max_num_of_nodes = 60
	G = prepare_data_to_graph.prepare_data_to_graph(filenames, path, max_num_of_nodes)

	# dodawanie hashu commita do grafu
	commit_hash = get_git_commit_hash(path)
	G.attr(label='Lastest commit hash: ' + commit_hash)
	G.attr(fontsize='20')

	G.view()


if __name__ == "__main__":
	files_dependency(sys.argv[1])
