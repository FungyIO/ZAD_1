import directory_filenames
import prepare_data_to_graph


def files_dependency():
	filenames = directory_filenames.get_current_directory_filenames()
	G = prepare_data_to_graph.prepare_data_to_graph(filenames)
	G.view()


if __name__ == "__main__":
	files_dependency()
