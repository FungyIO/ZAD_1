import parse_functions_names
import directory_filenames


def parse_function():
    files = directory_filenames.get_current_directory_filenames()
    nodes = []

    for file in files:
        nodes_from_file = parse_functions_names.parse_function(file)
        for node in nodes_from_file:
            nodes.append(node)

    return nodes
